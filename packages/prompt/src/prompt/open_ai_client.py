from openai import AzureOpenAI

from .env import env

class ChatbotOpenAI :
    def __init__(self, key=env.AZURE_OPENAI_KEY, endpoint=env.AZURE_OPENAI_ENDPOINT, deployment=env.AZURE_OPENAI_DEPLOYMENT_NAME, embedding=env.AZURE_OPENAI_EMBEDDING_NAME) -> None:
        self.client = AzureOpenAI(api_key=key, api_version ="2024-02-01", azure_endpoint =endpoint)
        self.deployment_name = deployment
        self.embedding = embedding
        self.last_response = ""
    
    def chatHistory(self, chat_history) :
        return [{"role": role, "content": message} for role, message in chat_history]
    
    def query(self, query="", system="", chat_history=[], temperature=0, tools=None, tool_choice=None) :
        chat_history = self.chatHistory(chat_history)
        system = [{"role": "system", "content": system}] if system else []
        query = [{"role":"user", "content":query}] if query else []
        messages = system + chat_history + query

        try :
            completion = self.client.chat.completions.create(
                model=self.deployment_name,
                temperature=temperature,
                messages=messages,
                tools=tools,
                tool_choice=tool_choice,
            )
        except Exception as e:
            print(e)
            return 1
        
        if tools :
            response = completion.choices[0].message.tool_calls[0].function.arguments
        else :
            response = completion.choices[0].message.content
            self.last_response = response

        return response

    def stream(self, query="", system="", chat_history=[], temperature=0) :
        chat_history = self.chatHistory(chat_history)
        system = [{"role": "system", "content": system}] if system else []
        query = [{"role":"user", "content":query}] if query else []
        messages = system + chat_history + query

        self.last_response = ""

        try :
            for chunk in self.client.chat.completions.create(
                model=self.deployment_name,
                temperature=temperature,
                messages=messages,
                stream=True
            ) :
                if chunk.choices != [] :
                    content = chunk.choices[0].delta.content
                    if content is not None:
                        self.last_response += content
                        yield content.replace('\n','<br>').replace('\t', '    ')

        except Exception as e:
            print(e)
            return 1

    def vectorize(self, message) :
        try :
            response = self.client.embeddings.create(input=message, model=self.embedding)

        except Exception as e:
            print(e)
            return 1
        
        return response.data[0].embedding
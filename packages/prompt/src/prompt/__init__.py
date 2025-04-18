from prompt.open_ai_client import ChatbotOpenAI

def hello():
    return "Hello World"

def apples():
    open_ai_client = ChatbotOpenAI()
    return open_ai_client.query("What is an apple ?")
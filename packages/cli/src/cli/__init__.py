import typer
from prompt import apples as prompt_apples
app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    formal = typer.confirm("Are you sure?", default=False)
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

def main() -> None:
    app()

@app.command()
def apples():
    print(prompt_apples())
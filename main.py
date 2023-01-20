import typer
import requests
from utils.functions import generateRandomStrings

app = typer.Typer()


@app.command()
def generateRanomString(templength: int):
    print(templength)
    length = 5 if templength < 5 else templength
    print(generateRandomStrings(length))


@app.command()
def generateUrl():
    print("https://blazeurl.ly/sadsjh")


if __name__ == "__main__":
    app()

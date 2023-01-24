import typer
import requests
from utils.functions import generateRandomStrings
from utils.db import DBHandler
from dotenv import dotenv_values

app = typer.Typer()

config = dotenv_values(".env")


@app.command()
def generate(templength: int):
    print(config)

    length = 5 if templength < 5 else templength
    mongo = DBHandler()
    print(mongo)
    print(generateRandomStrings(length))


@app.command()
def generateUrl():
    print("https://blazeurl.ly/sadsjh")


if __name__ == "__main__":
    app()

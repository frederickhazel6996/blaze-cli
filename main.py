import typer
import webbrowser
import requests
import os
import validators
from utils.functions import generateRandomStrings
from utils.db import MongoHandler
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()
BASE_URL = os.getenv("BASE_URL")


@app.command()
def shortenurl(url: str):

    validation = validators.url(url)
    if validation is not True:
        print("URL is not valid")
        return 0

    mongo = MongoHandler()
    tempIdentifier = generateRandomStrings(7)
    loop = True

    with mongo:
        while loop:
            urls = mongo.db["cliurls"].find_one({"identifier": tempIdentifier})
            if urls is None:
                loop = False
                tempUrlData = {"original_url": url, "identifier": tempIdentifier}
                mongo.db["cliurls"].insert_one(tempUrlData)
                print(f"Short URL is {BASE_URL}{tempIdentifier}")
                return 1


@app.command()
def fetchurl(url: str):
    validation = validators.url(url)
    if validation is not True:
        print("URL is not valid")
        return
    mongo = MongoHandler()
    tempIdentifier = url[len(BASE_URL) :]
    with mongo:
        tempurl = mongo.db["cliurls"].find_one({"identifier": tempIdentifier})
        print(tempurl["original_url"])


@app.command()
def openurl(url: str):
    validation = validators.url(url)
    if validation is not True:
        print("URL is not valid")
        return
    mongo = MongoHandler()
    tempIdentifier = url[len(BASE_URL) :]
    with mongo:
        tempurl = mongo.db["cliurls"].find_one({"identifier": tempIdentifier})
        webbrowser.open(tempurl["original_url"])


if __name__ == "__main__":
    app()

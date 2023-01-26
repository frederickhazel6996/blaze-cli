import typer
import requests
import validators
from utils.functions import generateRandomStrings
from utils.db import MongoHandler
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()


@app.command()
def shorten(url: str):

    validation = validators.url(url)
    print(validation)
    if validation is not True:
        print("URL is not valid")
        return

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
                print(f"Short URL is https://blazeurl.ly/{tempIdentifier}")


@app.command()
def openurl():
    print("https://blazeurl.ly/sadsjh")


if __name__ == "__main__":
    app()

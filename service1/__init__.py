import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters = requests.get('https://mile2.azurewebsites.net/api/service2?code=5Oe3dW0aRWIT3f7OyzYu7E3sY1FMndtZiYNWvHRlxn6ERQKun5APAw==')
    numbers = requests.get('https://mile2.azurewebsites.net/api/service3?code=fzzgiaDqjvqb0M/hq4yMKiOrGzemhE6ZBZ/1DILkwdf6oPxMmzltpA==')


    return func.HttpResponse(
        str(letters.text+numbers.text),
        status_code=200
    )

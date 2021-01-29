import logging
import string
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    for n in range(5):
        let = random.choice(string.ascii_letters)
        letters += str(let)

    return func.HttpResponse(
        str(letters),
        status_code=200
    )

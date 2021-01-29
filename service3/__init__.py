import logging
import string
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    for i in range(5):
        num = random.randint(0,9)
        numbers += str(num)

    return func.HttpResponse(
        str(numbers),
        status_code=200
    )
import requests
import azure.functions as func
import logging
from src.service.quotable_service import QuotableService

from src.exceptions.exception_handler import exception_handler


@exception_handler
def get_random_quote(req: func.HttpRequest) -> func.HttpResponse:
    try:
        quote_service = QuotableService()
        random_quote = quote_service.get_random_quote()
        return func.HttpResponse(
            body=random_quote.to_json(), status_code=200, mimetype="application/json"
        )
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve quotes. Exception: {str(e)}")
        error_message = "Failed to retrieve quotes. Please try again later."
        return func.HttpResponse(body=error_message, status_code=500)

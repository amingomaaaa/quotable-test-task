import requests
import azure.functions as func
import logging
from src.service.quotable_service import QuotableService
from src.exceptions.exception_handler import exception_handler


@exception_handler
def get_filtered_quote(req: func.HttpRequest) -> func.HttpResponse:
    try:
        quote_service = QuotableService()
        filtered_quote = quote_service.get_filtered_quote("les")
        return func.HttpResponse(filtered_quote, status_code=200)
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve quotes. Exception: {str(e)}")
        error_message = "Failed to retrieve quotes. Please try again later."
        return func.HttpResponse(body=error_message, status_code=500)

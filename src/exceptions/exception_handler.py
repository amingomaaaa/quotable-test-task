import logging
from functools import wraps
from typing import Any, Callable

import requests
from azure.functions import HttpResponse


def exception_handler(func: Callable) -> Callable:
    """
    Decorator function that handles exceptions raised within the wrapped function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(e)
            return HttpResponse(body=f'An error occurred while processing', status_code=400)

    return wrapper

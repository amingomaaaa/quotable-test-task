import json
import logging
from dataclasses import asdict, dataclass
from typing import List, Optional

import requests

from src.service.quotable_api_client import QuotableAPIClient


@dataclass
class Quote:
    _id: str
    content: str
    author: str
    tags: list
    authorSlug: str
    length: int
    dateAdded: str
    dateModified: str

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        quote_dict = self.to_dict()
        return json.dumps(quote_dict)


class QuotableService:
    _API_CLIENT = QuotableAPIClient()

    @classmethod
    def get_random_quote(cls) -> Quote:
        """Retrieve a random quote from the Quotable API"""
        try:
            response = cls._API_CLIENT.send_get_request("random")
            if response.status_code == 200:
                random = response.json()
                return Quote(**random)
            else:
                logging.error(
                    f"Failed to retrieve quotes. Status code: {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred while sending the API request: {str(e)}")

    @classmethod
    def get_filtered_quote(cls, particle: str) -> Optional[List[Quote]]:
        """Retrieve quotes containing a specified particle in the author's name"""
        try:
            response = cls._API_CLIENT.send_get_request("quotes")
            if response.status_code == 200:
                quotes = response.json()
                filtered_quotes = [
                    Quote(**quote)
                    for quote in quotes["results"]
                    if particle in quote["author"].lower()
                ]
                return filtered_quotes
            else:
                logging.error(
                    f"Failed to retrieve quotes. Status code: {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred while sending the API request: {str(e)}")



a = QuotableService()

c = a.get_random_quote()

print(c)
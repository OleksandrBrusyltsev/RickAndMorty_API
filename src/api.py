import os
import requests

from data_processor import DataProcessor
from logger import Logger
from dotenv import load_dotenv
from typing import Any, Dict, List, Optional

from dataclass import Character, Location, Episode
import logging.config
import logging

logging.config.fileConfig('logging.ini')

load_dotenv()


class APIService:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def send_request(self, url: str) -> Optional[Dict[str, Any]]:
        """
        Send a request to the API and retrieve the JSON response.
        """

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.exception(f"Error during request: {e}")
            return None


class RickAndMortyAPI:
    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def fetch_obj(self, obj: str) -> List[Dict[str, Any]]:
        """Fetch objects from the API."""

        results = []
        url = f'{self.api_service.base_url}/{obj}'

        while url:
            data = self.api_service.send_request(url)
            if data:
                results.extend(data.get('results', []))
                url = data.get('info', {}).get('next')
            else:
                break

        return results

    def get_characters(self) -> List[Character]:
        """Retrieve characters data from the API."""
        character_data = self.fetch_obj('character')
        return [Character(**char) for char in character_data]

    def get_locations(self) -> List[Location]:
        """Retrieve characters data from the API."""
        location_data = self.fetch_obj('location')
        return [Location(**loc) for loc in location_data]

    def get_episodes(self) -> List[Episode]:
        """Retrieve characters data from the API."""
        episode_data = self.fetch_obj('episode')
        return [Episode(**ep) for ep in episode_data]


def main():
    base_url = os.getenv("BASE_URL")
    api_service = APIService(base_url)

    connector = RickAndMortyAPI(api_service)

    objects = ['character', 'location', 'episode']

    mapping = {
        'character': Character,
        'location': Location,
        'episode': Episode
    }

    for obj in objects:
        data = connector.fetch_obj(obj)
        DataProcessor.process_data(data, obj, mapping)

    episodes_data = connector.get_episodes()
    locations_data = connector.get_locations()

    episodes_logger = Logger()
    locations_logger = Logger()

    episodes_result = episodes_logger.log_episodes_year(episodes_data)
    logging.info("Episodes aired between 2017 and 2021 with more than three characters: %s", episodes_result)

    locations_result = locations_logger.log_locations(episodes_data, locations_data)
    logging.info("Locations that appear only on odd episode numbers: %s", locations_result)


if __name__ == "__main__":
    main()

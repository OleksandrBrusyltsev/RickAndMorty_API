import os

import requests
from data_processor import DataProcessor
from logger import Logger
from dotenv import load_dotenv

load_dotenv()


class APIService:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during request: {e}")
            return None


class APIConnector:
    def __init__(self, api_service):
        self.api_service = api_service

    def fetch_all_data(self, endpoint):
        results = []
        url = endpoint
        while url:
            data = self.api_service.send_request(url)
            if data:
                results.extend(data['results'])
                url = data['info']['next']
            else:
                break
        return results


class RickAndMortyAPI(APIConnector):
    pass


def main():
    base_url = os.getenv("BASE_URL")
    api_service = APIService(base_url)

    connector = APIConnector(api_service)

    objects = ['character', 'location', 'episode']
    for obj in objects:
        data = connector.fetch_all_data(obj)
        DataProcessor.process_data(data, obj)

    episodes_data = DataProcessor.process_data(connector.fetch_all_data('episode'), 'episode')
    locations_data = DataProcessor.process_data(connector.fetch_all_data('location'), 'location')

    Logger.log_episodes(episodes_data)
    Logger.log_locations(episodes_data, locations_data)


if __name__ == "__main__":
    main()

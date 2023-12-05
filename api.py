import requests
from data_processor import DataProcessor
from logger import Logger


class APIConnector:
    BASE_URL = "https://rickandmortyapi.com/api"

    def fetch_all_data(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        results = []
        while url:
            response = requests.get(url)
            data = response.json()
            results.extend(data['results'])
            url = data['info']['next']
        return results


class RickAndMortyAPI(APIConnector):
    pass



def main():
    api = RickAndMortyAPI()
    characters = api.fetch_all_data('character')
    locations = api.fetch_all_data('location')
    episodes = api.fetch_all_data('episode')

    processor = DataProcessor()
    processor.process_data(characters, 'characters')
    processor.process_data(locations, 'locations')
    processor.process_data(episodes, 'episodes')

    logger = Logger()
    logger.log_episodes(episodes)
    logger.log_locations(episodes, locations)


if __name__ == "__main__":
    main()

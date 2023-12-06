import unittest
from unittest.mock import MagicMock, patch

from api import APIService, RickAndMortyAPI
from data_processor import DataProcessor
from dataclass import Character, DetailCharacter


class TestRickAndMortyAPI(unittest.TestCase):
    def test_character_creation(self):
        char = Character(id=1, name='Rick Sanchez', status='Alive', species='Human', type='', gender='Male',
                         origin=DetailCharacter(name='Earth', url='https://...'),
                         location=DetailCharacter(name='Earth', url='https://...'),
                         image='https://...', episode=['https://...'], url='https://...',
                         created='2017-11-04T18:48:46.250Z')
        self.assertEqual(char.name, 'Rick Sanchez')
        self.assertEqual(char.status, 'Alive')
        self.assertEqual(char.species, 'Human')
        self.assertEqual(char.type, '')
        self.assertEqual(char.gender, 'Male')
        self.assertEqual(char.origin.name, 'Earth')

    def test_format_data(self):
        char = Character(id=1, name='Rick Sanchez', status='Alive', species='Human', type='', gender='Male',
                         origin=DetailCharacter(name='Earth', url='https://...'),
                         location=DetailCharacter(name='Earth', url='https://...'),
                         image='https://...', episode=['https://...'], url='https://...',
                         created='2017-11-04T18:48:46.250Z')
        formatted_data = DataProcessor._format_data(char)
        self.assertIn('Metadata', formatted_data)
        self.assertIn('RawData', formatted_data)

    @patch('requests.get')
    def test_send_request(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'results': [{'name': 'Rick Sanchez'}]}
        mock_get.return_value = mock_response

        api_service = APIService('https://rickandmortyapi.com/api')
        response = api_service.send_request('https://rickandmortyapi.com/api/character')
        self.assertIsNotNone(response)
        self.assertEqual(response['results'][0]['name'], 'Rick Sanchez')

    def test_fetch_obj(self):
        mock_api_service = MagicMock()
        mock_api_service.send_request.return_value = {'results': [{'name': 'Rick Sanchez'}]}
        rick_morty_api = RickAndMortyAPI(mock_api_service)
        results = rick_morty_api.fetch_obj('character')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], 'Rick Sanchez')

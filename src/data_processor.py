import json
import os
import uuid
from dataclasses import asdict

from src.dataclass import Character, Location, Episode


class DataProcessor:
    @staticmethod
    def save_json(data, filename):
        formatted_data = []

        for item in data:

            generated_id = str(uuid.uuid4())

            metadata = item.name if isinstance(item, (Character, Location, Episode)) else ""

            raw_data = asdict(item)

            formatted_item = {
                'Id': generated_id,
                'Metadata': metadata,
                'RawData': raw_data
            }
            formatted_data.append(formatted_item)

        result_directory = 'result'
        if not os.path.exists(result_directory):
            os.makedirs(result_directory)

        file_path = os.path.join(result_directory, filename)
        with open(file_path, 'w') as file:
            json.dump(formatted_data, file, indent=2)

    @staticmethod
    def process_data(raw_data, data_type):
        processed_data = []

        mapping = {
            'character': Character,
            'location': Location,
            'episode': Episode
        }

        for item in raw_data:
            if data_type in mapping:
                processed_data.append(mapping[data_type](**item))

        DataProcessor.save_json(processed_data, f"{data_type}.json")

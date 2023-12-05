import json
import uuid


class DataProcessor:
    @staticmethod
    def save_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
    @staticmethod
    def process_data(raw_data, data_type):
        processed_data = [{
            'Id': str(uuid.uuid4()),
            'Metadata': item['name'],
            'RawData': item
        } for item in raw_data]
        DataProcessor.save_json(processed_data, f"{data_type}.json")


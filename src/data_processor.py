import json

import os
import uuid
from dataclasses import asdict
from typing import List, Union

from dataclass import Character, Location, Episode
import logging.config
import logging
logging.config.fileConfig('logging.ini')

class DataProcessor:
    result_directory = 'result'

    @staticmethod
    def _format_data(data: Union[Character, Location, Episode]) -> dict:
        """Formats data into a dictionary.

        Args:
            data (Union[Character, Location, Episode]): The data to format.

        Returns:
            dict: The formatted data.
        """
        generated_id = str(uuid.uuid4())
        metadata = getattr(data, 'name', '')
        raw_data = asdict(data)

        formatted_item = {
            'Id': generated_id,
            'Metadata': metadata,
            'RawData': raw_data
        }
        return formatted_item

    @staticmethod
    def save_json(data: List[Union[Character, Location, Episode]], filename: str) -> None:
        """Saves data as JSON.

        Args:
            data (List[Union[Character, Location, Episode]]): The data to save.
            filename (str): The name of the output file.
        """
        try:
            formatted_data = [DataProcessor._format_data(item) for item in data]

            if not os.path.exists(DataProcessor.result_directory):
                os.makedirs(DataProcessor.result_directory)

            file_path = os.path.join(DataProcessor.result_directory, filename)
            with open(file_path, 'w') as file:
                json.dump(formatted_data, file, indent=2)

        except FileNotFoundError as e:
            logging.error(f"Directory not found: {e}")

    @staticmethod
    def process_data(raw_data: List[dict], data_type: str, mapping: dict) -> None:
        """Processes raw data and saves it as JSON.

        Args:
            raw_data (List[dict]): The raw data to process.
            data_type (str): The type of data.
            mapping (dict): The mapping for data processing.
        """
        processed_data = []

        try:
            for item in raw_data:
                if data_type in mapping:
                    processed_data.append(mapping[data_type](**item))

            DataProcessor.save_json(processed_data, f"{data_type}.json")

        except KeyError as e:
            logging.error(f"Key not found: {e}")

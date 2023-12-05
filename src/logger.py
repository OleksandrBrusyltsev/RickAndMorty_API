import logging.config
import logging
from typing import List, Optional
from dateutil import parser
from dataclass import Episode, Location

logging.config.fileConfig('logging.ini')


class Logger:
    @staticmethod
    def log_episodes_year(episodes: Optional[List[Episode]]) -> List[str]:
        """Logs episodes within a certain date range, with specific character count."""
        episode_names = []
        try:
            if episodes:
                filtered_episodes = filter(
                    lambda eps: (
                            2017 <= parser.parse(eps.air_date).year <= 2021
                            and len(eps.characters) > 3
                    ),
                    episodes
                )
                for episode in filtered_episodes:
                    episode_names.append(episode.name)
        except Exception as e:
            logging.exception(f"Error logging episodes: {e}")
        return episode_names


    @staticmethod
    def log_locations(episodes: Optional[List[Episode]], locations: Optional[List[Location]]) -> List[str]:
        """Logs locations based on episode characteristics.

        Args:
            episodes (Optional[List[Episode]]): List of episodes.
            locations (Optional[List[Location]]): List of locations.

        Returns:
            List[str]: List of location names.
        """
        location_names = []
        try:
            if episodes and locations:
                odd_episodes = {episode.id for episode in episodes if int(episode.episode.split('E')[-1]) % 2 != 0}

                odd_episode_locations = set()
                for location in locations:
                    if all(location.url not in episode.characters for episode in episodes if
                           episode.id in odd_episodes):
                        odd_episode_locations.add(location.name)

                location_names = list(odd_episode_locations)
        except Exception as e:
            logging.exception(f"Error logging locations: {e}")
        return location_names

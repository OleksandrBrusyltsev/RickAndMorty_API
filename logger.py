class Logger:
    @staticmethod
    def log_episodes(episodes):
        filtered_episodes = filter(
            lambda eps: "2017" <= eps.get('air_date', '')[:4] <= "2021" and len(eps.get('characters', [])) > 3,
            episodes
        )
        print("Episodes between 2017 and 2021 with more than three characters:")
        for episode in filtered_episodes:
            print(episode['name'])

    @staticmethod
    def log_locations(episodes, locations):
        odd_episodes = {episode['id'] for episode in episodes if int(episode['episode'].split('E')[-1]) % 2 != 0}

        odd_episode_locations = set()
        for location in locations:
            if any(location['url'] in episode['characters'] for episode in episodes if
                   episode['id'] in odd_episodes):
                odd_episode_locations.add(location['name'])

        print("Locations appearing only in odd-numbered episodes:")
        for location in odd_episode_locations:
            print(location)

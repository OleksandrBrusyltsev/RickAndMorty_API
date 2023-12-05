# RickAndMorty API Integration

![RickAndMorty](https://i.gifer.com/fyHf.gif)
<p>
    <img src="![image]([https://github.com/OleksandrBrusyltsev/RickAndMorty_API/assets/124603897/47d621f2-5618-4efc-9099-1a6009cbf50f](https://i.gifer.com/fyHf.gif))
" alt="RickAndMorty GIF">
</p>


This project serves as an integration client for the RickAndMorty API, allowing the retrieval of specific objects and processing of their data.

## Objective

The objective of this project is to create an integration client that:

1. Retrieves data for the following objects from the RickAndMorty API:
   - Character
   - Location
   - Episode
2. Outputs the data for each object to separate JSON files with the following fields:
   - Id: Generated GUID
   - Metadata: Name from within the fetched object
   - RawData: The fetched JSON data presented as a dictionary
3. Prints to the screen:
   - A log of episodes aired between 2017 and 2021, containing more than three characters.
   - A list of locations that appear only in odd-numbered episodes (e.g., episodes 1, 3, 9).

## Usage

### Installation

1. Ensure Python is installed.
2. Clone this repository.
3. install Poetry:
```bash
pip install poetry
```
4.Install the required dependencies:
   ```bash
    poetry insall
   ```
5.Navigate to the source directory:
```bash
cd src
```

6.Run the main script to execute the integration client:
 ```bash
    python api.py
   ```

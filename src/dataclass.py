from dataclasses import dataclass
from typing import List


@dataclass
class DetailCharacter:
    name: str
    url: str

@dataclass
class Character:
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: DetailCharacter
    location: DetailCharacter
    image: str
    episode: List[str]
    url: str
    created:str


@dataclass
class Location:
    id: int
    name: str
    type: str
    dimension: str
    residents: List[str]
    url: str
    created: str


@dataclass
class Episode:
    id: int
    name: str
    air_date: str
    episode: str
    characters: List[str]
    url: str
    created: str




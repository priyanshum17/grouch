import json
from pathlib import Path
from typing import List

from pydantic import BaseModel

CONFIG_PATH = Path("grouch/config/settings.json")


class Configuration(BaseModel):
    """
    A Pydantic model to represent the overall configuration.

    Attributes:
        link (str): URL to Oscar's Course Status Page
        fodder_words (List[str]): A list of all fodder words.

    """

    link: str
    fodder_words: List[str]


settings = json.load(open(CONFIG_PATH, "r"))
config = Configuration(**settings)

print(config)

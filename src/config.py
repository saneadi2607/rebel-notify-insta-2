from typing import List
import os
import yaml
import json


class Config:
    def __init__(self):
        with open("config.yml", "r") as stream:
            self.data = os.environ

    @property
    def webhook_url(self) -> str:
        return os.environ['webhook_url']

    @property
    def users(self) -> List[str]:
        return json.loads(os.environ['users'])

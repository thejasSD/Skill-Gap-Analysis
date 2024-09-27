import json
import re

from utility.logger import logger


class JsonExtractor:
    def __init__(self):
        self.pattern = r'\{[^{}]*\}'

    def prepare_proper_json(self):
        pass


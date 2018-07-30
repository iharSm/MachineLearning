import json
from pprint import pprint
import os


class Context:

    def __init__(self):
        self.context = {}
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        with open(ROOT_DIR + "\\config.json") as f:
            config = json.load(f)
        pprint (config)

        #TODO: map config file to the context
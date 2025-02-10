import json
import os

import yaml


def get_file_extension(filepath):
    return os.path.splitext(filepath)[-1][1:].lower()


def load_file(filepath):
    extension = get_file_extension(filepath)

    with open(filepath, "r", encoding="utf-8") as file:
        if extension in ["json"]:
            return json.load(file)
        elif extension in ["yml", "yaml"]:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {extension}")

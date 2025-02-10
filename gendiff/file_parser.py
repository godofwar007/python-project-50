import json
import os

import yaml


def load_file(filepath):
    _, ext = os.path.splitext(filepath)
    with open(filepath, 'r') as f:
        if ext.lower() == '.json':
            return json.load(f)
        elif ext.lower() in ['.yaml', '.yml']:
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

import json
import os

import yaml


def parse_data(data, ext):
    ext = ext.lower()
    handlers = {
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml'
    }
    if ext in handlers:
        format = handlers[ext]
        if format == 'json':
            return json.loads(data)
        elif format in ['yaml', 'yml']:
            return yaml.safe_load(data)
    raise ValueError(f"Unsupported file extension: {ext}")


def load_file(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    ext = os.path.splitext(filepath)[1]
    return parse_data(data, ext)

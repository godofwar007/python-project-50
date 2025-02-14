import json
import os

import yaml


def parse_data(data, format):
    format = format.lower()
    if format == 'json':
        return json.loads(data)
    elif format in ['yaml', 'yml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unsupported format: {format}")


def load_file(filepath):
    handlers = {
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml'
    }

    with open(filepath, 'r') as f:
        data = f.read()

    ext = os.path.splitext(filepath)[1].lower()

    if ext in handlers:
        return parse_data(data, handlers[ext])

    raise ValueError(f"Unsupported file extension: {ext}")

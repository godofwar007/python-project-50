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
    with open(filepath, 'r') as f:
        data = f.read()
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    if ext == '.json':
        return parse_data(data, 'json')
    elif ext in ['.yaml', '.yml']:
        return parse_data(data, 'yaml')
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

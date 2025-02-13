from gendiff.format.json import format_json
from gendiff.format.plain import format_plain
from gendiff.format.stylish import format_stylish


def select_format(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")

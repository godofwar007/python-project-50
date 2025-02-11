from gendiff.diff_builder import build_diff
from gendiff.file_parser import load_file
from gendiff.format.json import format_json
from gendiff.format.plain import format_plain
from gendiff.format.stylish import format_stylish


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")
    
    
    
    
    
    

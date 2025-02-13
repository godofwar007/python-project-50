from gendiff.diff_builder import build_diff
from gendiff.file_parser import load_file
from gendiff.format.select_format import select_format


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)
    diff = build_diff(data1, data2)
    return select_format(diff, format_name)

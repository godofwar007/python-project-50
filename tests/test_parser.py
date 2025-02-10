import os

from gendiff.generate_diff import generate_diff

BASE_DIR = os.path.dirname(__file__)
FILE1_PATH = os.path.join(BASE_DIR, "test_data", "file1.json")
FILE2_PATH = os.path.join(BASE_DIR, "test_data", "file2.json")
EXPECTED_OUTPUT_PATH = os.path.join(
    BASE_DIR, "test_data", "expected_output.txt")


def test_generate_diff():
    with open(EXPECTED_OUTPUT_PATH) as expected:
        expected_output = expected.read().strip()

    assert generate_diff(FILE1_PATH, FILE2_PATH).strip() == expected_output

import pytest

from gendiff.generate_diff import generate_diff


@pytest.fixture
def file_paths():
    return "tests/test_data/file1.json", "tests/test_data/file2.json"


def test_generate_diff(file_paths):
    file1, file2 = file_paths
    with open("tests/test_data/expected_output.txt") as expected:
        expected_output = expected.read().strip()

    assert generate_diff(file1, file2).strip() == expected_output

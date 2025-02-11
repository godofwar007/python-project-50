import os

import pytest

from gendiff.generate_diff import generate_diff

BASE_DIR = os.path.dirname(__file__)


@pytest.fixture
def json_files():
    return (
        os.path.join(BASE_DIR, "test_data", "file1.json"),
        os.path.join(BASE_DIR, "test_data", "file2.json")
    )


@pytest.fixture
def expected_output():
    with open(os.path.join(
            BASE_DIR, "test_data", "expected_output.txt"), "r") as f:
        return f.read().strip()


@pytest.fixture
def expected_output_plain():
    with open(os.path.join(
            BASE_DIR, "test_data", "expected_output_plain.txt"), "r") as f:
        return f.read().strip()


@pytest.fixture
def expected_output_json():
    with open(os.path.join(BASE_DIR, "test_data",
                           "expected_output_json.txt"), "r") as f:
        return f.read().strip()


def test_diff_json_stylish(json_files, expected_output):
    file1, file2 = json_files
    result = generate_diff(file1, file2, "stylish").strip()
    assert result == expected_output


def test_diff_json_plain(json_files, expected_output_plain):
    file1, file2 = json_files
    result = generate_diff(file1, file2, "plain").strip()
    assert result == expected_output_plain


def test_diff_json_format(json_files, expected_output_json):
    file1, file2 = json_files
    result = generate_diff(file1, file2, "json").strip()
    assert result == expected_output_json

import os

import pytest

from gendiff.generate_diff import generate_diff

BASE_DIR = os.path.dirname(__file__)


@pytest.fixture
def json_file_paths():
    return (
        os.path.join(BASE_DIR, "test_data", "file1.json"),
        os.path.join(BASE_DIR, "test_data", "file2.json"),
    )


@pytest.fixture
def yaml_file_paths():
    return (
        os.path.join(BASE_DIR, "test_data", "file1.yml"),
        os.path.join(BASE_DIR, "test_data", "file2.yml"),
    )


@pytest.fixture
def expected_output():
    with open(os.path.join(
            BASE_DIR, "test_data", "expected_output.txt")) as expected:
        return expected.read().strip()


def test_diff_json(json_file_paths, expected_output):
    file1, file2 = json_file_paths

    assert generate_diff(file1, file2).strip() == expected_output


def test_diff_yaml(yaml_file_paths, expected_output):
    file1, file2 = yaml_file_paths
    assert generate_diff(file1, file2).strip() == expected_output


@pytest.fixture
def yaml_files():
    return "tests/test_data/file1.yml", "tests/test_data/file2.yml"


def test_generate_yaml2(yaml_files, expected_output):
    file1, file2 = yaml_files
    assert generate_diff(file1, file2) == expected_output

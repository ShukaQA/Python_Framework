from typing import Any, Iterable

from framework.logger import logger


def assert_status_code(response: Any, expected: int):
    """
    Assert that the response status code matches the expected value.

    Args:
        response: Response object with a `.status_code` attribute.
        expected: Expected HTTP status code.
    """
    actual = response.status_code
    if actual != expected:
        logger.error(f"Unexpected status code. Expected {expected}, got {actual}")
    assert actual == expected, f"Expected status code {expected}, got {actual}"


def assert_json_has_keys(response_json: dict, keys: Iterable[str]):
    """
    Assert that the JSON response contains all the required keys.

    Args:
        response_json: JSON object (dict) from API response.
        keys: Iterable of keys expected to be present in response_json.
    """
    missing_keys = [key for key in keys if key not in response_json]
    if missing_keys:
        logger.error(f"Missing keys in response JSON: {missing_keys}")
    assert not missing_keys, f"Missing keys in response JSON: {missing_keys}"

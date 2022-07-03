"""Test cases for the __main__ module."""
import pytest

from {{cookiecutter.package_name}} import __main__


@pytest.fixture
def runner() -> None:
    """Fixture for invoking command-line interfaces."""
    __main__.hello()


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    assert 0 == 0

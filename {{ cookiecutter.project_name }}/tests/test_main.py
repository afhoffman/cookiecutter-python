"""Test cases for the cli module."""
import pytest

from {{cookiecutter.package_name}} import cli


@pytest.fixture
def runner() -> None:
    """Fixture for invoking command-line interfaces."""
    cli.hello()


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    assert 0 == 0

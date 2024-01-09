import pytest

from players_manager.players import Singleton


@pytest.fixture(autouse=True)
def reset_singletons():
    Singleton._instances = {}

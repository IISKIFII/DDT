import pytest


from .sender_link import SenderLink
from .sender_link import LOGGER


@pytest.fixture
def logger():
    return LOGGER


@pytest.fixture(scope="module")
def sender():
    sender_link = SenderLink()
    return sender_link

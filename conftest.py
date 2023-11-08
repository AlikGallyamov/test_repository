import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_open():
    browser.config.window_width = 800
    browser.config.window_height = 1024


import pytest
from selene import browser


@pytest.fixture
def browser_open():
    browser.config.window_width = 1690
    browser.config.window_height = 1080

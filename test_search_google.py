from selene.support.shared import browser
from selene import be, have


import pytest


@pytest.fixture
def browser_open():
    browser.config.window_width = 800
    browser.config.window_height = 1024
    browser.open('https://google.com')
    # yield
    # browser.clear_session_storage()
    # browser.close()




def test_search_1(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_2(browser_open):
    browser.element('[name="q"]').should(be.blank).type('asdasdqw123asdsadfgqwdaswqdfsa213f').press_enter()
    browser.element('[class ="Gfzyee VDgVie jREHUb R1smN Pjsr7c"]').click()

    if browser.element('[aria-label="Поиск"]'):
        browser.element('[aria-label="Поиск"]').click()

    assert browser.element('[class="card-section"]').should(have.text(' ничего не найдено. '))



from selene import be, have, browser


def test_search_1(browser_open):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_2(browser_open):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asdasdqw123asdsadfgqwdaswqdfsa213f').press_enter()
    browser.element('[class ="Gfzyee VDgVie jREHUb R1smN Pjsr7c"]').click()

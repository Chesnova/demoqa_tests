from selene.support.shared import browser


def set_button(number: int):
    browser.element(f'#gender-radio-{number}').double_click()
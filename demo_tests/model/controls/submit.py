from selene.support.shared import browser
from selene import command


def submit_form():
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # browser.element('#submit').perform(command.js.click)
    browser.element('#submit').submit()
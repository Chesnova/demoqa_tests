from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demo_tests.model.controls import modal, radiobutton, datepicker, submit
from tests.test_data import users
from tests.test_data.users import Subject
from demo_tests.utils import path


def given_opened(value: str):
    browser.open(value)
    ads = browser.element('[id^=google_ads][id$=container__]')
    if (
        ads.with_(timeout=6)
        .wait.until(have.size_greater_than_or_equal(3))
    ):
        ads.perform(command.js.remove)


def set_name(value):
    browser.element('#firstName').set_value(value)


def set_last_name(value):
    browser.element('#lastName').type(value)


def set_user_email(value):
    browser.element('#userEmail').type(value)


def fill_gender(value: users.Gender):
    radiobutton.set_button(value.value)


def set_birthday(day, month, year):
    datepicker.fill_date(day, month, year)


# def set_birthdate(day, month, year):
#     datepicker.set_date(day, month, year)


def set_user_number(value):
    browser.element('#userNumber').type(value)


def add_user_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def add_user_hobbies(values):
    # browser.element('[for="hobbies-checkbox-3"]').click()
    for hobby in values:
        browser.all('[id^=hobbies').by(have.value(hobby.value)).first.element(
            '..'
        ).click()


def upload_file(value):
    browser.element('#uploadPicture').send_keys(path.to_resource(value))


def set_address(value):
    browser.element('#currentAddress').set_value(value)


def fill_dropdown(option, value):
    browser.element(f'#react-select-{option}-input').type(value).press_enter()


def submit_form():
    submit.submit_form()


def should_have_submitted(data):
    rows = modal.content.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))

    # browser.element('.table-responsive').all('tbody tr').should(have.texts
import pytest
import os
from selene.support.shared import browser
from selene import have, command, by
from selene.support.shared.jquery_style import ss
from tests.test_data.users import first_user


def given_open_browser():
    browser.open('/automation-practice-form')
    # (
    #     ss('[id^=google_ads][id$=container__]').with_(timeout=10)
    #     .should(have.size_greater_than_or_equal(3))
    #     .perform(command.js.remove)
    # )


def test_student_registration_form():
    given_open_browser()

    # WHEN
    browser.element('#firstName').set_value(first_user.name)
    browser.element('#lastName').type(first_user.last_name)
    browser.element('#userEmail').set_value(first_user.email)
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').set_value(first_user.user_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(first_user.birth_month)
    browser.element('.react-datepicker__year-select').send_keys(first_user.birth_year)
    browser.element(f'.react-datepicker__day.react-datepicker__day--0{first_user.birth_day}').click()
    # browser.element('#subjectsInput').type(subject.value).press_enter().type(subject.value).press_enter()
    for subject in first_user.subjects:
        browser.element('#subjectsInput').type(subject.value).press_enter()
    # browser.element('[for="hobbies-checkbox-3"]').click()
    for hobby in first_user.hobbies:
        browser.all('[id^=hobbies').by(have.value(hobby.value)).first.element(
            '..'
        ).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/fortest.png'))
    browser.element('#currentAddress').set_value('Figueres, Catalonia, Spain')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()

    # THEN
    browser.element('.table-responsive').all('tbody tr').should(have.texts(
        'Student Name Salvador Dali',
        'Student Email test@test.test',
        'Gender Male', 'Mobile 9999999999',
        'Date of Birth 11 April,2000',
        'Subjects Computer Science, Biology',
        'Hobbies Music',
        'Picture fortest.png',
        'Address Figueres, Catalonia, Spain',
        'State and City Haryana Karnal'
    ))
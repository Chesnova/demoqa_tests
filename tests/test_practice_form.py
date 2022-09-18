import pytest
import os
from selene.support.shared import browser
from selene import have

@pytest.fixture
def open_browser():
    browser.config.timeout = 3
    browser.config.base_url = ('https://demoqa.com')


def test_student_registration_form(open_browser):
    # adding text in the registration form
    browser.open('/automation-practice-form')
    browser.element('#firstName').set_value('Salvador')
    browser.element('#lastName').type('Dali')
    browser.element('#userEmail').set_value('test@test.test')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').set_value('9999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('April')
    browser.element('.react-datepicker__year-select').send_keys('2000')
    browser.element('.react-datepicker__day.react-datepicker__day--011').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter().type('Biology').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/fortest.png'))
    browser.element('#currentAddress').set_value('Figueres, Catalonia, Spain')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()

    # assert modal form
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
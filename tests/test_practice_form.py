import pytest
from selene.support.shared import browser
from selene import have, be

@pytest.fixture
def open_browser():
    browser.config.timeout = 3
    browser.config.base_url = ('https://demoqa.com')

def test_student_registration_form(open_browser):
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
    # browser.with_(timeout=3).element('#dateOfBirthInput').should(have.value('11 Apr 2000'))
    browser.element('#subjectsInput').type('Computer Science').press_enter().type('Biology').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys()

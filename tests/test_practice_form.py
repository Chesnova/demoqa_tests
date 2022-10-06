from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demo_tests.model.pages import registration_form as app
from demo_tests.utils import attach
from tests.test_data.users import student
import allure
from allure_commons.types import Severity


def test_student_registration_form():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Student registration form")
    allure.dynamic.story("filling out the registration form")
    allure.dynamic.link("https://demoqa.com", name="Testing")
    with allure.step("Open main page"):
        app.given_opened('/automation-practice-form')

    with allure.step("Filling out the registration form"):
        app.set_name(student.name)
        app.set_last_name(student.last_name)
        app.set_user_email(student.email)
        app.fill_gender(student.gender.Male)
        app.set_user_number(student.user_number)
        app.set_birthday(student.birth_day, student.birth_month, student.birth_year)
        app.add_user_subjects(student.subjects)
        app.add_user_hobbies(student.hobbies)
        app.upload_file(student.picture_file)
        app.set_address(student.currentAddress)
        app.fill_dropdown(3, student.state)
        app.fill_dropdown(4, student.city)
        app.submit_form()

    with allure.step("Сhecking the completed form"):
        app.should_have_submitted(
            [
                ('Student Name', 'Salvador Dali'),
                ('Student Email', 'test@test.test'),
                ('Gender', 'Male'),
                ('Mobile', '9999999999'),
                ('Date of Birth', '11 April,2000'),
                ('Subjects', 'Computer Science, Biology'),
                ('Hobbies', 'Music'),
                ('Picture', 'fortest.png'),
                ('Address', 'Figueres, Catalonia, Spain'),
                ('State and City', 'Haryana Karnal')
            ],
        )

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
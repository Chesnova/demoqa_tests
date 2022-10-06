from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def set_date(day: str, month: str, year: str):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL+'a').type(day+month+year).press_enter()


def fill_date(day, month, year):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()




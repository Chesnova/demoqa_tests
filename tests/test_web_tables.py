import pytest
from selene.support.shared import browser
from selene import have

def given_open_browser():
    browser.open('/webtables')

def test_add_fourth_line():
    given_open_browser()
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Salvador')
    browser.element('#lastName').type('Dali')
    browser.element('#userEmail').set_value('test@test.test')
    browser.element('#age').type('31')
    browser.element('#salary').type('5000')
    browser.element('#department').type('Insurance')
    browser.element('#submit').submit()

    # assert table
    browser.all('.rt-tr-group')[3].all('.rt-td').should(have.texts(
        'Salvador', 'Dali', '31', 'test@test.test', '5000', 'Insurance', ''
    ))

def test_edit_all_fields_second_line():
    given_open_browser()
    browser.element('#edit-record-2').click()
    browser.element('#firstName').clear().type('Salvadorito')
    browser.element('#lastName').clear().type('Dalila')
    browser.element('#userEmail').clear().set_value('test3@test.test')
    browser.element('#age').clear().type('31')
    browser.element('#salary').clear().type('6000')
    browser.element('#department').clear().type('Insurance')
    browser.element('#submit').submit()

    # assert table
    browser.all('.rt-tr-group')[1].all('.rt-td').should(have.texts(
        'Salvadorito', 'Dalila', '31', 'test3@test.test', '6000', 'Insurance', ''
    ))


def test_remove_third_line():
    given_open_browser()
    browser.element('#delete-record-3').click()

    # assert table
    browser.all('.rt-tr-group')[2].all('.rt-td').should(have.no.texts(
        'Kierra', 'Gentry', '29', 'kierra@example.com', '2000', 'Legal', ''
    ))
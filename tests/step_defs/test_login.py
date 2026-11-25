from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when

from config import settings

scenarios("login.feature")


@given("I am on the login page")
def open_login_page(login_page):
    login_page.open()


@when("I log in with valid credentials")
def login_valid(login_page):
    login_page.login(settings.VALID_EMAIL, settings.VALID_PASSWORD)


@when(parsers.re(r'I log in with email "(?P<email>[^"]*)" and password "(?P<password>[^"]*)"'))
def login_with(login_page, email, password):
    login_page.login(email, password)


@then(parsers.parse('I should see the "{text}" heading'))
def see_heading(login_page, text):
    expect(login_page.heading).to_have_text(text)


@then(parsers.parse('I should see the error "{message}"'))
def see_error(login_page, message):
    expect(login_page.error_message).to_contain_text(message)


@then("I should be on the dashboard")
def on_dashboard(dashboard_page):
    dashboard_page.should_be_open()
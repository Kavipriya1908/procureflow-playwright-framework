import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    path = "/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Welcome back")
        self.email_input = page.get_by_placeholder("you@company.com")
        self.password_input = page.get_by_placeholder("••••••••")
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.error_message = page.locator(".auth-err")
        self.forgot_password_link = page.get_by_role("link", name="Forgot password?")

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        self.email_input.fill(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.password_input.fill(password)

    @allure.step("Click Sign In")
    def click_sign_in(self):
        self.sign_in_button.click()

    @allure.step("Log in as {email}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in()
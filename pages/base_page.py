from playwright.sync_api import Page

from config import settings


class BasePage:
    path = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(settings.BASE_URL + self.path)
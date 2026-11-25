import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
class DashboardPage(BasePage):
    path = "/dashboard"

    def __init__(self, page:Page ):
        super().__init__(page)

    def should_be_open(self):
        expect(self.page).to_have_url(re.compile(r".*/dashboard$"))
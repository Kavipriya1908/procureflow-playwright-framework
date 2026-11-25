from playwright.sync_api import Playwright

from config import settings

class AuthAPI:
    def __init__(self, playwright: Playwright):
         self.request = playwright.request.new_context(base_url=settings.API_BASE_URL)

    def login(self, email, password):
        response = self.request.post(
            "/api/auth/login",
            data={"email": email, "password": password},
        )
        return response

    def close(self):
        self.request.dispose()
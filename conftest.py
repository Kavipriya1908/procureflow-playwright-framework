import allure

from utils.logger import get_logger

import pytest
from api.auth_api import AuthAPI
from config import settings
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
log = get_logger("tests")

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)


def pytest_collection_modifyitems(config, items):
    if settings.has_credentials():
        return
    skip = pytest.mark.skip(reason="Add VALID_EMAIL and VALID_PASSWORD to .env")
    for item in items:
        if "needs_credentials" in item.keywords:
            item.add_marker(skip)

@pytest.fixture(scope="session")
def auth_api(playwright):
    api = AuthAPI(playwright)
    yield api
    api.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    log.info("%s -> %s", item.name, report.outcome.upper())

    page = item.funcargs.get("page")
    if report.failed and page is not None:
        allure.attach(
            page.screenshot(full_page=True),
            name="Screenshot on failure",
            attachment_type=allure.attachment_type.PNG,
        )
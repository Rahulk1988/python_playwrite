import pytest
from playwright.sync_api import sync_playwright

<<<<<<< HEAD
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
=======
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.wait_for_timeout(3000)
>>>>>>> ac181d6523a29b752126a7aab8ace7c786c1081a
        yield page
        browser.close()
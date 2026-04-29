from pages.google_page import GooglePage
from utils.logger import get_logger

def test_google(page):
    google = GooglePage(page)
    google.open()
    assert "Google" in google.get_title()


logger = get_logger()
logger.info("Test started")
from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in page.url
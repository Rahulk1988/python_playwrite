from pages.login_page import LoginPage


def test_invalid_login(page):
    login = LoginPage(page)
    login.load()
    login.login("wrong", "wrong")

    assert "error" in page.content()
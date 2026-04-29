from pages.cart_page import CartPage
from pages.login_page import LoginPage


def test_add_to_cart(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)
    cart.add_item()
    cart.go_to_cart()

    assert "cart" in page.url
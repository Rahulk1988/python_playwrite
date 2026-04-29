class CartPage:
    def __init__(self, page):
        self.page = page

    def add_item(self):
        self.page.click("text=Add to cart")

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")
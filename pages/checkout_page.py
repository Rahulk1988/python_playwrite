class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.click("#checkout")
        self.page.fill("#first-name", "Rahul")
        self.page.fill("#last-name", "Test")
        self.page.fill("#postal-code", "12345")
        self.page.click("#continue")
        self.page.click("#finish")
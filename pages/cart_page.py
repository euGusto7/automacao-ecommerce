from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self):
        self.click(self.ADD_TO_CART)

    def open_cart(self):
        self.click(self.CART_ICON)

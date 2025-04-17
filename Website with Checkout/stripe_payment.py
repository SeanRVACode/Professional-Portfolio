import stripe
import os
from dotenv import load_dotenv
from icecream import ic
from decimal import Decimal

load_dotenv()


class Stripe:
    def __init__(self):
        # FIXME Finish setting this up
        self.base_url = "https://api.stripe.com"
        # Becomes a global api key I believe
        stripe.api_key = os.getenv("stripe_api_key")

    def charge_payment(self):
        pass

    def get_products(self):
        products = stripe.Product.list()
        # For Debugging Print Products List
        ic(products)
        if len(products) > 0:
            for product in products["data"]:
                product["default_price"] = self.get_price(product["default_price"])
                ic(product["default_price"])
        return products

    def get_price(self, price_code):
        price = stripe.Price.retrieve(price_code)
        actual_price = Decimal(price["unit_amount_decimal"]) / 100
        return actual_price

    def list_all_prices(self):
        prices = stripe.Price.list()
        ic(prices)


if __name__ == "__main__":
    payment = Stripe()
    payment.get_products()

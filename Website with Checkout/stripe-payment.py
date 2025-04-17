import stripe
import os
from dotenv import load_dotenv

load_dotenv()


class Stripe:
    def __init__(self):
        # FIXME Finish setting this up
        self.base_url = "https://api.stripe.com"
        # Becomes a global api key I believe
        stripe.api_key = os.getenv("stripe_api_key")

    def charge_payment(self):
        pass


if __name__ == "__main__":
    payment = Stripe()

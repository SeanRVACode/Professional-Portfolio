from shop.api.stripe_payment import Stripe


class StripeUtils:
    def __init__(self):
        self.stripe = Stripe()

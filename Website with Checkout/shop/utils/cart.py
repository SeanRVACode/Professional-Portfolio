from shop import stripe


class Cart:
    def __init__(self, session):
        self.session = session
        self.cart = session.get("cart", {})
        self.cart_details = session.get("cart_details", {})

    def add_to_cart(self, item_id_str, product_data):
        # Gets the item ID as a string that was passed from the form.,
        if item_id_str in self.cart:
            self.cart[item_id_str] += 1
        else:
            self.cart[item_id_str] = 1
            # Store Product Details
            self.cart_details[item_id_str] = {
                "name": product_data.name,
                "price": stripe.get_price(product_data.default_price),
            }
        self.session.modified = True

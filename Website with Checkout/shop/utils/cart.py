from shop import stripe
from icecream import ic


class Cart:
    def __init__(self, session):
        self.session = session
        self.cart = session.get("cart", {})
        self.cart_details = session.get("cart_details", {})

    def add_to_cart(self, item_id_str, product_data):
        ic(item_id_str)
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

    def update_cart(self, product_id_str, action):
        if product_id_str and action and "cart" in self.session:
            if action == "increase":
                self.session["cart"][product_id_str] += 1
            elif action == "decrease":
                if self.session["cart"][product_id_str] > 1:
                    self.session["cart"][product_id_str] -= 1
                else:
                    # Remove the item completely
                    self.session["cart"].pop(product_id_str)

            elif action == "remove":
                # Completely removes the item regardless of quantity
                self.session["cart"].pop(product_id_str)

            self.session.modified = True

    def convert_to_line_item(self):
        line_items = [
            {"price": stripe.get_single_product(item_id)["default_price"], "quantity": quantity}
            for item_id, quantity in self.session["cart"].items()
        ]
        return line_items

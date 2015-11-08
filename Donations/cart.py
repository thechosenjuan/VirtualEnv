
class CartItem(object)

	def __init__(self, product, quantity, price):
	    self.product = product
	    self.quantity = int(quantity)
	    self.price = Decimal(str(price))

class CartShopping(object)
	def __init__(self, session, session_key=None):
	    self._items_dict = []
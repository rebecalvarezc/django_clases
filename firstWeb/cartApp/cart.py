class Cart:
    """
    This class contains all the functions needed to have a shopping cart on a web page.
    """

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            # {clave (id del prod): {valor (características del producto)}}
            cart = self.session['cart'] = {}

        # else:
        self.cart = cart

    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'quantity': 1,
                'image': product.picture.url
            }

        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] += 1
                    value['price'] = value['quantity'] * float(product.price)

                    break
        self.safe_cart()

    def safe_cart(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def delete(self, product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.safe_cart()

    def remove(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] -= 1
                value['price'] = value['price'] - float(product.price)
                if value['quantity'] < 1:
                    self.delete(product)
                    break
        self.safe_cart()

    def clean_cart(self):
        self.session['cart'] = {}
        self.session.modified = True

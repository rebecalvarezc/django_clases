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

        else:
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
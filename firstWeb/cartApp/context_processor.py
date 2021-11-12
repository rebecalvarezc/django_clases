def total_cart_value(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total += float(value['price']*value['quantity'])
    return {'total_cart_value': total}

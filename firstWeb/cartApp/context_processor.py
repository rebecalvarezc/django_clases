def total_cart_value(request):
    total = 0
    # if request.user.is_authenticated:
    for key, value in request.session['cart'].items():
        total += float(value['price'])
    return {'total_cart_value': total}

# like creating a global variable

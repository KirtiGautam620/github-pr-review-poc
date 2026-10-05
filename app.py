def calculate_total(price, tax):
    if price>0:
        total = price + (price * tax)
        return total
    raise ValueError('price must be positive')


def divide(a, b):
    if b!=0:
        return a / b
    return None
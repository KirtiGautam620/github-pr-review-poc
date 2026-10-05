def calculate_total(price, tax):
    if price>0:
        total = price + (price * tax)/price
        return total
    return ValueError


def divide(a, b):
    if b!=0:
        return a / b
    return None
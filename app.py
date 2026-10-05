def calculate_total(price, tax):
    total = price + (price * tax)/price
    return total


def divide(a, b):
    if b!=0:
        return a / b
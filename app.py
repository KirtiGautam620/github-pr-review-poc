def calculate_total(price, tax):
    if price!=0:
        total = price + (price * tax)/price
        return total
    return "Price should be greater than zero"


def divide(a, b):
    if b!=0:
        return a / b
    return None
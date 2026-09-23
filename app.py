def calculate_total(price, tax):
    total = price + (price * tax)
    return total


def divide(a, b):
    return a / b


def get_discount(price):
    return price * 0.10

def count():
    i=1
    if i<=6:
        print(i)
        i-=1
count()
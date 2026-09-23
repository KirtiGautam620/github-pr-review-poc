def calculate_total(price, tax):
    total = price + (price * tax)
    return total


def divide(a, b):
    return a / b


def get_discount(price):
    return price * 0.10

def count_numbers():
    i = 1

    while i <= 5:
        print(i)

count_numbers()
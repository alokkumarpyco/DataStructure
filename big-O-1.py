# big(o) 1 example

def add_items_1(n):
    return n + n


def add_items_2(n):
    return n + n + n


if __name__ == "__main__":
    print(add_items_1(10))
    print(add_items_2(10))
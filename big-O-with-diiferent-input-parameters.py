# Here function takes 2 different parameters
# so it will be O(a) + O(b) --> O(a + b)

def add_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)


if __name__ == "__main__":
    add_items(10, 20)
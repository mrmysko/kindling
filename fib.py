def main():

    while True:
        length = input("How long fib? ")
        if length.isdigit():
            length = int(length)
            break

    fib(length)


def fib(length):

    a, b = 0, 1
    while a < length:
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    main()

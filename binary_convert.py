# Convert decimal to binary.


def main():

    b = False
    d = False

    while True:
        choice = input("Convert to (b)inary or (d)ecimal?: ")
        if choice[0] == "b":
            b = True
            break
        elif choice[0] == "d":
            d = True
            break

    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            break

    if b == True:
        binary = ""
        while number != 0:

            if number % 2 == 0:
                binary += "0"
            else:
                binary += "1"
            number = number // 2
        print(binary[::-1])

    if d == True:
        list_binary = list(str(number))

        deci_sum = 0
        for power, i in enumerate(reversed(list_binary)):
            if i == "1":
                deci_sum += 2**power
        print(deci_sum)


if __name__ == "__main__":
    main()

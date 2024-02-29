def main():

    while True:
        bill = input("Bill amount: ")
        if bill.isdigit():
            bill = int(bill)
            break
    while True:
        tip = input("Tip percent: ")
        if tip.isdigit():
            tip = int(tip)
            break

    tip_total = round(tip_amount(bill, tip), 2)
    bill_total = round(bill + tip_total, 2)

    print(f"The tip amount is: {tip_total}, total bill is: {bill_total}")


def tip_amount(bill, tip_percent=10):
    """Calculate the tip amount."""
    return bill * (tip_percent / 100)


if __name__ == "__main__":
    main()

# Rashelle Ward
# CIS261
# Invoice Line Item Calculator

def getprice():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Try again.")

def getquantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Try again.")

def main():
    print("Invoice Line Item Calculator\n")

    answer = "y"
    while answer.lower() == "y":
        price = getprice()
        quantity = getquantity()
        total = price * quantity

        print()
        print("Price:   ", f"{price: .2f}")
        print("Quantity:    ", quantity)
        print("Total:   ", f"{total: .2f}")
        answer = input("Enter another item? (y/n): ")
        print()

    print("Goodbye!")

if __name__ == "__main__":
    main()

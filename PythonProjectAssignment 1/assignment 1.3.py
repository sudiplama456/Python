def main():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0
    print("Supermarket")
    print("===========")

    while True:
        try:
            product_number = int(input("Please select product (1-10) 0 to Quit: "))
            if product_number == 0:
                break
            elif 1 <= product_number <= 10:
                price = prices[product_number - 1]
                total_sum += price
                print(f"Product: {product_number} Price: {price}")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input.")

    print(f"Total: {total_sum}")
    try:
        payment = float(input("Payment: "))
        if payment >= total_sum:
            print(f"Change: {payment - total_sum}")
        else:
            print("Insufficient payment.")
    except ValueError:
        print("Invalid payment.")


if __name__ == "__main__":
    main()
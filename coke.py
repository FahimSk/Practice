def main():
    due = 0
    left = 50
    coins = [5, 10, 25]
    print("Amount Due: 50")

    while due < 50:
        insert = int(input("Input Coin: "))

        while insert not in coins:
            print("Invalid coin. Please insert 5, 10, or 25 cents.")
            insert = int(input("Input Coin: "))

        due = due + insert
        left = left - insert

        if due > 50:
            print(f"Change owed: {abs(left)}")
        else:
            print(f"Amount Due: {left}")

main()

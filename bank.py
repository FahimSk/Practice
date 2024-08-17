def main():
    bank = input("Greeting: ").lower().strip()

    if bank == "hello" or bank == "hello there" or bank == "hello, Newman":
        print("$0")
    elif bank != "" and bank[0] == "h":
        print("$20")
    else:
        print("$100")

main()

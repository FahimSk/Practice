def day():
    response = input("How was your day? ").replace(" ", " ... ")
    main(response)

def main(n):
    print("x:", n)

day()

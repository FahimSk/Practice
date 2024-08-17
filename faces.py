def convert():
    emoji = input("Please enter: :) or :( \n"). replace(":)", "🙂").replace(":(", "😐")
    main(emoji)

def main(n):
    print(n)

convert()


def main():
    question = input("What is the 'Great Question of Life, the Universe and Everything'? ").lower()

    if question == "42":
        print("Yes")
    elif question == "forty-two":
        print("Yes")
    elif question == "forty two":
        print("Yes")
    else:
        print("No")

main()


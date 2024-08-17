def main():
    vowels = ["a", "e", "i", "o", "u"]

    vowels = str(vowels)

    answer = input("Input: ")

    for vowel in vowels:
        if answer not in vowels:
            answer = answer.replace(vowels, "")
            print(f"Output: {answer}")

main()



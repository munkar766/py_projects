def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    m = [x for x in word if x not in vowels]
    return "".join(m)


if __name__ == "__main__":
    main()

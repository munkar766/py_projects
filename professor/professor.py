import random


def main():
    level = get_level()
    score = 0

    
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        add = x + y

        tries = 0
        while tries < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == add:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1


        if tries == 3:
            print(f"{x} + {y} = {add}")

    # Output final score for check50
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()

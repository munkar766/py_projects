import random

def main():
    while True:
        try:
            level = int(input('level: '))
            if level <= 0:
                int('ok')
        except ValueError:
            pass
        else:
            break

    ans = random.randint(1, level)
    while True:
        try:
            guess = int(input('guess: '))
            if guess <= 0:
                int('ok')
        except ValueError:
            pass
        else:

            if guess == ans:
                print("Just right!")
                return 0
            elif guess > ans:
                print('Too large!')
            elif guess < ans:
                print("Too small!")













main()

import random
import cowsay




def main():
    result1 = 'you won!'
    result2 = 'you lost!'
    result3 = 'its a draw'
    win1= 0
    lose1 = 0

    options = ['rock', 'paper', 'scissors']

    threshold = 5

    cowsay.cow('Welcome to Rock, Paper, Scissors!!!!!!!')
    while True:
        enter = input('Enter rock, paper or scissors: ').lower()
        option = random.choice(options)
        enter = valid(enter, options)
        while enter == None:
            print('You gotta choose among those 3 given options')
            enter = input('Enter rock, paper or scissors: ').lower()
            enter = valid(enter, options)
        if result1 == win(enter, option):
            print(result1)
            win1 += 1
        elif result2 == lose(enter, option):
            print(result2)
            lose1 += 1
        elif result3 == draw(enter, option):
            print(result3)

        if win1 == threshold:
            print('------------------You have won the game!------------------')
            cowsay.cow('GAME OVER!')
            break
        elif lose1 == threshold:
            print('--------------------You have lost the game!-----------------')
            cowsay.cow('GAME OVER!')
            break


def valid(enter, options):



    if enter not in options:
        return None
    else:
        return enter


def win(enter, option):

    if (enter == 'rock' and option == 'scissors') or (enter == 'paper' and option == 'rock') or  (enter == 'scissors' and option == 'paper'):

        return ('you won!')


def lose(enter, option):

    if (enter == 'rock' and option == 'paper') or (enter == 'paper' and option == 'scissors') or  (enter == 'scissors' and option == 'rock'):


        return ('you lost!')

def draw(enter, option):
    if enter == option:
        return ('its a draw')





if __name__ == "__main__":
    main()
    
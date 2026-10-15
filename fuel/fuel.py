
def main():
    while True:
        i = input("fraction: ")

        while '/' not in i:
            i = input("fraction: ")

        i = list(i)


        i.append('0')
        find = (i.index("/"))
        first_number = [x for x in i[0:find]]
        last_number = [x for x in i[(find+1):-1]]
        first_number = ''.join(first_number)

        last_number = ''.join(last_number)

        try:
            first_number = int(first_number)
            last_number = int(last_number)
            if first_number<0 or last_number<0 or first_number>last_number:
                int('invalid')
            percentage = (first_number/last_number)*100


        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            first_number = int(first_number)
            last_number = int(last_number)

            percentage = round((first_number/last_number)*100)
            if percentage <= 1:
                print("E")
                return 0
            elif percentage >= 99:
                print("F")
                return 0
            else:
                print(f'{percentage}%')
                return 0




main()






import inflect
p = inflect.engine()


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            print(f'Adieu, adieu, to {p.join((names))}')
            return 0
        else:
            names.append(name)

















main()

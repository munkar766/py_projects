import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$', s):
        h1, m1, meridian1, h2 , m2, meridian2 = match.groups()
        m1 = int(m1) if m1 else 0
        m2 = int(m2) if m2 else 0
        if int(m1) >= 60 and int(m2) >= 60:
            raise ValueError
        else:
            h1 = int(h1)
            h2 = int(h2)

            if meridian1 == 'AM' and meridian2 == 'AM':
                return f'{h1:02}:{m1:02} to {h2:02}:{m2:02}'
            elif meridian1 == 'PM' and meridian2 == 'AM':

                h1 += 12
                return f'{h1:02}:{m1:02} to {h2:02}:{m2:02}'
            elif meridian1 == 'AM' and meridian2 == 'PM':
                if h1 == 12 and h2==12:
                    h1 -= 12
                    
                    return f'{h1:02}:{m1:02} to {h2:02}:{m2:02}'


                else:
                    h2 += 12
                    return f'{h1:02}:{m1:02} to {h2:02}:{m2:02}'
            elif meridian1 == 'PM' and meridian2 == 'PM':

                h1 += 12
                h2 += 12
                return f'{h1:02}:{m1:02} to {h2:02}:{m2:02}'



    else:
        raise ValueError


...


if __name__ == "__main__":
    main()

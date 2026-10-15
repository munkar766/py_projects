from datetime import date
import inflect
import sys
import re
p = inflect.engine()


def main():
    z = input('Date of Birth: ')

    try:

        mins = get_mins(z)
    except ValueError:
        sys.exit('Invalid date')
    else:
        words = p.number_to_words(mins, wantlist = False).replace(" and", '').capitalize()
        print(f'{words} minutes')



def get_mins(s):
    match = re.search(r'^(\d{4})-(\d{2})-(\d{2})$', s)
    if match:
        years, months, days = match.groups()
        years = int(years)
        months = int(months)
        days = int(days)
        dob = date(years, months, days)
        today = date.today()
        delta = today - dob
        delta = delta.days
        return delta*24*60

    else:
        raise ValueError('Invalid date')


    ...


if __name__ == "__main__":
    main()

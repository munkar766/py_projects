def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

    month_dict = {
        'January' : 1,
        "February" : 2,
        "March" :3,
        "April":4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    while True:
        date = input("date: ").strip()

        if '/' in date:


            month, day, year = date.split('/')
            try:
                if month.isalpha():
                    int('invalid')
            except ValueError:
                pass
            else:
                month = int(month)
                day = int(day)
                try:
                    if month > 12 or day > 31:
                        int('invalid')
                except ValueError:
                    pass
                else:
                    new_date= print(f'{year}-{(month):02}-{(day):02}')
                    return 0





        elif ',' in date and '/' not in date:
            try:

                date1 = date.replace(',', '').replace(" ", "-")
                m, d, y = date1.split('-')
                date_list1 = [m, d, y]



                if len(date_list1[1]) > 2:
                    int('invalid')
            except ValueError:
                pass
            else:

                date = date.replace(',', '').replace(" ", "-")
                month, day, year = date.split('-')
                month = month.capitalize()
                day = int(day)
                try:
                    if day > 31:
                        int('invalid')
                except ValueError:
                    pass
                else:
                    print(f'{year}-{(month_dict.get(month)):02}-{(day):02}')
                    return 0







main()

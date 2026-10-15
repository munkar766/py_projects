def main():
    time = input ('What time is it? ')
    t = convert(time)


    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    time = time.strip()
    hours, seconds = time.split(":")
    t = float(hours) + float(seconds)/60
    return t





if __name__ == "__main__":
    main()

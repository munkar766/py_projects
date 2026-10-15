def main():
    while True:
        try:
            user_input = input("fraction: ")
            percentage = convert(user_input)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    fraction = list(fraction)
    fraction.append("0")
    find = fraction.index("/")
    first_number = [x for x in fraction[0:find]]
    last_number = [x for x in fraction[(find + 1) : -1]]
    first_number = "".join(first_number)
    last_number = "".join(last_number)

    first_number = int(first_number)
    last_number = int(last_number)

    if last_number == 0:
        raise ZeroDivisionError

    if first_number < 0 or last_number < 0 or first_number > last_number:
        raise ValueError

    percentage = round((first_number / last_number) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

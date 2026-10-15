def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")




def slice(plate):
    header = plate.rstrip('0123456789') #plate='askdnbehdn09908'
    trailer = plate[len(header):]

    if header.isalpha() == False:
        return False
    elif trailer!='':
        if trailer[0] == '0':
            return False
        else:
            return True

    else:
        return True

def space(plate):
    import string
    punctuation_ = string.punctuation
    punctuation = list(punctuation_)
    presence = [x for x in plate if x in punctuation_]
    presence = ''.join(presence)


    if plate.find(".") != -1:
        return False
    elif plate.find(" ") != -1:
        return False
    elif len(presence) != 0:
        return False
    else:
        return True







def is_valid(plate):
    plate1 = list(plate)

    plate2 = [x for x in plate1[0:2]]

    plate2 = ''.join(plate2)
    if plate2.isalpha():
        if len(plate) >= 2 and len(plate) <= 6:
            if slice(plate):
                if space(plate):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    else:
        return False


main()

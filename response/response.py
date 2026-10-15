import validators

enter = input("What's your email address? ")

if validators.email(enter):
    print('Valid')
else:
    print('Invalid')



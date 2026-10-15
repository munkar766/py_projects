z = input("camelCase: ")

result=''

for x in z:
    if x.isupper():
        result += '_' + x.lower()

    else:
        result += x

print(f'Snakecase: {result}')







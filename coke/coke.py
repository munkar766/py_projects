

total = 0
remain = 50

print(f'amount due: {remain}')

while total<50:

    z = int(input('insert coin:(25/10/5): '))
    if z in [5,10,25]:
        total += z
        remain -= z
        if remain > 0:
            print(f"amount due: {remain}")
        else:
            break






change_owed= total - 50
print(f'change owed: {change_owed}')











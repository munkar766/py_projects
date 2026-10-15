import sys

proto = []

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')

try:
    with open(sys.argv[1]) as file:
        for line in file:
            proto.append(line)

            ans = [x for x in proto if not x.strip().startswith('#') and x.strip()]
    print(len(ans))







except FileNotFoundError:
    sys.exit('File does not exist')

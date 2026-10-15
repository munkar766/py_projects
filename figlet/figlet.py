
import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    z = input ("Input: ")
    y = figlet.renderText(z)
    print(y)
else:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        figlet.setFont(font=sys.argv[2])
        z = input ("Input: ")
        y = figlet.renderText(z)
        print(y)
    else:
        sys.exit('invalid')

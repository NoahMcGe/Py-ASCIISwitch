#Noah McGehee 11/24/23 noahmcge.xyz
from termcolor import colored, cprint
class Link:
    def __init__(self):
        self.b1 = 1
        self.b2 = 1
        self.b3 = 1
        self.b4 = 0
        self.b5 = 2
        self.b6 = 1

        self.x1 = "1"
        self.x2 = "2"
        self.x3 = "3"
        self.x4 = "4"
        self.x5 = "5"
        self.x6 = "6"

        self.d1 = ""
        self.d2 = ""
        self.d3 = ""
        self.d4 = ""
        self.d5 = ""
        self.d6 = ""

def main():
    loopmain()

def loopmain():
    link = Link()
    print("\n" * 100)
    print("         Pretend Switch.\n")
    printmap(link)

def printmap(link):
    print("      ", end= ' ')
    for x in range(1, 7):
        if getattr(link, 'b{}'.format(x)) == 1:
            cprint(getattr(link, 'x{}'.format(x)), 'red', attrs=['blink'], end='   ')
        elif getattr(link, 'b{}'.format(x)) == 0:
            cprint(getattr(link, 'x{}'.format(x)), 'red', attrs=['dark'], end='   ')
        elif getattr(link, 'b{}'.format(x)) == 2:
            cprint(getattr(link, 'x{}'.format(x)), 'red', end='   ')
    print('''
    ⢰⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⡆
    ⢸⣿⣿⡁⣹⣿⣿⡁⣹⣿⣿⡁⣹⣿⣿⡁⣹⣿⣿⡁⣹⣿⣿⡁⣹⣿⣿⡇
    ⠈⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁''')

if __name__ == '__main__':
    main()


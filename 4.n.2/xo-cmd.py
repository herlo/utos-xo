import getopt, sys
import random


def usage():
    print """
    Usage: xo-cmd.py    
"""

def check(guess, num):
    count = 0
    guess.reverse()
    num.reverse()
    print "guess" + str(guess)
    print "num" + str(num)
    
    for i in guess:
        print "guess: " + i
        print "num: " + num[count]
        if i == str(num[count]):
            count = count + 1
        else:
            return count

def main():
#    number = random.randrange(0,100000);
    
    number = list(str(54321))
    guess1 = list(str(54321))
    chk = check(guess1, number)
    print chk

    number = list(str(421))
    guess2 = list(str(441))
    chk = check(guess2, number)
    print chk
#    if chk:
#        print "success"
#    else:
#        print "fail"

    powers = "8x100 + 5x10 + 3x1"
    powers = "_x100 + 5x__ + 3x_"

if __name__ == "__main__":
    main()

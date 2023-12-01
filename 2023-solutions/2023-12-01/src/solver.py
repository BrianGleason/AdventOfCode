import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

class Solver:
    def __init__():
        pass

    def solve(path):
        file = open(path)
        lines = file.readlines()
        string = file.read()
        strippedlines = []
        splitlines = []
        split_char = " "

        for line in lines:
            stripped = line.strip()
            strippedlines.append(stripped)
            split = line.split(split_char)
            splitlines.append(split)

        print(strippedlines)

        val_dict = {"1":1, 
                    "2":2,
                    "3":3,
                    "4":4,
                    "5":5,
                    "6":6,
                    "7":7,
                    "8":8,
                    "9":9,
                    "0":0,
                    "one":1, 
                    "two":2,
                    "three":3,
                    "four":4,
                    "five":5,
                    "six":6,
                    "seven":7,
                    "eight":8,
                    "nine":9,
                    "zero":0}

        result = 0
        for strrrr in strippedlines:
            rev = strrrr[::-1]
            min, minposn = None, None
            max, maxposn = None, None
            valmin, valmax = None, None
            for key, val in val_dict.items():
                posn = strrrr.find(key)
                posn2 = strrrr.rfind(key)
                if posn == -1:
                    continue
                if minposn == None or posn < minposn:
                    min = val_dict[key]
                    minposn = posn
                    valmin = key
                if maxposn == None or posn2 > maxposn:
                    max = val_dict[key]
                    maxposn = posn2
                    valmax = key


            strminmax = str(min) + str(max)
            result += int(strminmax)



        return result
    
    

        ### start program here






#soln = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2023-solutions\\2023-12-01\\input\\DEMO.txt')
#print(soln)

solndemo = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2023-solutions\\2023-12-01\\input\\DATA.txt')
print(solndemo)
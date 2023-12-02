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



soln = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-02\\input\\DEMO.txt')
print(soln)

solndemo = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-02\\input\\DATA.txt')
print(solndemo)
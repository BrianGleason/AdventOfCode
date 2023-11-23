import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

class Solver:
    def __init__():
        pass

    def getPoints(char):
        if char.isupper():
            return int(ord(char)) - 64 + 26
        else:
            return int(ord(char)) - 96
        
    def fillSet(sack, string):
        for char in string:
            sack.add(char)
        return sack

    def solve(path):
        l = IOHelpers.parse_by_newline(path, one_per_line=True)
        result = 0
        for str in l:
            ind = int((len(str) + 1) / 2)
            sack1, sack2 = str[0:ind], str[ind:len(str)]
            set1 = Solver.fillSet(set(), sack1)
            set2 = Solver.fillSet(set(), sack2)
            set3 = set1.intersection(set2)
            for item in set3:
                result += Solver.getPoints(item)
        return result
    
    def solve2(path):
        lines = IOHelpers.read_lines_stripped(path)
        index = 0
        result = 0
        while index < len(lines):
            line1, line2, line3 = lines[index], lines[index + 1], lines[index + 2]
            index += 3
            set1 = Solver.fillSet(set(), line1)
            set2 = Solver.fillSet(set(), line2)
            set3 = Solver.fillSet(set(), line3)
            trio_intersection = set1.intersection(set2).intersection(set3)

            for item in trio_intersection:
                result += Solver.getPoints(item)
        return result






soln = Solver.solve2('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-03\\input\\DATA.txt')
print(soln)
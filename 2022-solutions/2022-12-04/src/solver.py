import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

class Solver:
    def __init__():
        pass

    def solve(path):
        lines = IOHelpers.parse_by_newline(path, ",")
        result = 0
        for line in lines:
            range1, range2 = line
            range1 = range1.split("-")
            range2 = range2.split("-")
            start1, end1 = int(range1[0]), int(range1[1])
            start2, end2 = int(range2[0]), int(range2[1])
            if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
                result += 1
        return result
    
    def solve2(path):
        lines = IOHelpers.parse_by_newline(path, ",")
        result = 0
        for line in lines:
            range1, range2 = line
            range1 = range1.split("-")
            range2 = range2.split("-")
            start1, end1 = int(range1[0]), int(range1[1])
            start2, end2 = int(range2[0]), int(range2[1])
            if (start1 <= start2 and end1 >= start2) or (start2 <= start1 and end2 >= start1) or (end1 <= end2 and start2 <= end1) or (end2 <= end1 and start1 <= end2):
                result += 1
        return result




soln = Solver.solve2('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-04\\input\\DEMO.txt')
print(soln)

solndemo = Solver.solve2('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-04\\input\\DATA.txt')
print(solndemo)
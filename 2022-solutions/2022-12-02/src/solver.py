import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

d = dict()
d["r"] = "XA"
d["p"] = "YB"
d["s"] = "ZC"

d2 = dict()
d2["A"] = dict()
d2["B"] = dict()
d2["C"] = dict()

d2["A"]["X"] = d["s"][1]
d2["A"]["Y"] = d["r"][1]
d2["A"]["Z"] = d["p"][1]

d2["B"]["X"] = d["r"][1]
d2["B"]["Y"] = d["p"][1]
d2["B"]["Z"] = d["s"][1]

d2["C"]["X"] = d["p"][1]
d2["C"]["Y"] = d["s"][1]
d2["C"]["Z"] = d["r"][1]

class Solver:
    def __init__():
        pass

    def solve(source_file):
        input = IOHelpers.read_lines_stripped(source_file)
        score = 0
        turn_list = []
        for raw_input in input:
            m1, outcome = raw_input.split(" ")
            print(m1, outcome)
            m2 = d2[m1][outcome]
            turn_list.append((m1, m2))


        for turn in turn_list:
            m2, m1 = turn
            if m1 in d["r"]:
                score += 1
                if m2 in d["r"]:
                    score += 3
                elif m2 in d["p"]:
                    score += 0
                else:
                    score += 6
            elif m1 in d["p"]:
                score += 2
                if m2 in d["r"]:
                    score += 6
                elif m2 in d["p"]:
                    score += 3
                else:
                    score += 0
            elif m1 in d["s"]:
                score += 3
                if m2 in d["r"]:
                    score += 0
                elif m2 in d["p"]:
                    score += 6
                else:
                    score += 3  
            print(m2, m1)
        return score




soln = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-02\\input\\DATA.txt')
print(soln)
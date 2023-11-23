import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

class Solver:
    def __init__():
        pass

    def update_max_elf_cals_list(current, l):
        for i, cals in enumerate(l):
            if current > cals:
                if i == 0:
                    l[2] = l[1]
                    l[1] = l[0]
                    l[0] = current
                elif i == 1:
                    l[2] = l[1]
                    l[1] = current
                else:
                    l[2] = current
                return l
        return l

    def calorie_counting(source_file):
        input = IOHelpers.read_lines(source_file)
        max_elf_cals_list = [-1, -1, -1]
        current_elf_cals = 0
        for line_raw in input:
            line = line_raw.strip()
            if line == "":
                max_elf_cals_list = Solver.update_max_elf_cals_list(current_elf_cals, max_elf_cals_list)
                current_elf_cals = 0
            else:
                item_cals = int(line)
                current_elf_cals += item_cals
        return sum(max_elf_cals_list)



soln = Solver.calorie_counting('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-01\\input\\DATA.txt')
print(soln)
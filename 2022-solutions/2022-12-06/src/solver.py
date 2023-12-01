import sys
import os
import collections

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

class Solver:
    def __init__():
        pass
    def setHasKey(queue):
        s = set()
        for char in queue:
            s.add(char)
        return len(s) == 14

    def solve(path):
        queue = collections.deque()
        file = open(path)
        encoded = file.read()
        for index, char in enumerate(encoded):
            if len(queue) >= 14: queue.popleft()
            queue.append(char)
            if Solver.setHasKey(queue): return index
        return -1






soln = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-06\\input\\DEMO.txt')
print(soln)

solndemo = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-06\\input\\DATA.txt')
print(solndemo)
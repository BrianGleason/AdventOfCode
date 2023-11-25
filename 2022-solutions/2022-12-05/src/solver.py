import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

class Solver:
    def __init__():
        pass

    def parse_grid(grid):
        stacklist = [[], [], [], [], [], [], [], [], []]
        for str in grid:
            lstr = list(str)
            for index, char in enumerate(lstr):
                if index in (1, 5, 9, 13, 17, 21, 25, 29, 33) and char.isalpha():
                    stacklist[int((index - 1)/4) - 1].append(char)
        for stack in stacklist:
            stack.reverse()
        result  = [stacklist[8]]
        result.append(stacklist[0])
        result.append(stacklist[1])
        result.append(stacklist[2])
        result.append(stacklist[3])
        result.append(stacklist[4])
        result.append(stacklist[5])
        result.append(stacklist[6])
        result.append(stacklist[7])

        return result
    
    def parse_moves(moves):
        result = []
        for move in moves:
            spaced_moves = move.split(" ")
            count = spaced_moves[1]
            src = spaced_moves[3]
            dst = spaced_moves[5]
            result.append([count, src, dst])
        return result
    
    def execute_move(move, grid):
        count, src, dst = move
        for i in range(int(count)):
            if len(grid[int(src) - 1]) != 0:
                lifted = grid[int(src) - 1].pop()
                grid[int(dst) - 1].append(lifted)

    def execute_move_9001(move, grid):
        count, src, dst = move
        count = int(count)
        src = int(src) - 1
        dst = int(dst) - 1
        source_stack = grid[src]
        lifted = source_stack[len(source_stack) - count: len(source_stack)]
        grid[src] = source_stack[0:len(source_stack) - count]
        for element in lifted:
            grid[dst].append(element)
            


    def solve(path):
        lines_list = IOHelpers.read_lines_stripped(path)
        break_index = 0
        for index, line in enumerate(lines_list):
            if line == "":
                print(index)
                break_index = index
        grid = lines_list[0: break_index - 1]
        moves = lines_list[break_index + 1: len(lines_list)]
        grid = Solver.parse_grid(grid)
        moves = Solver.parse_moves(moves)

        for move in moves:
            #Solver.execute_move(move, grid)
            Solver.execute_move_9001(move, grid)
        res = ""
        for stack in grid:
            print(stack)
            res = res + stack.pop()
        return res





#soln = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-05\\input\\DEMO.txt')
#print(soln)

solndemo = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2022-solutions\\2022-12-05\\input\\DATA.txt')
print(solndemo)
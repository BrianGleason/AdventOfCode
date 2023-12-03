import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')))
sys.path.insert(0, 'C:\\Users\\gleas\\Projects\\AdventOfCode\\tools\\')

from iohelpers import IOHelpers

class Solver:
    def __init__():
        pass

    def build_adjacent_grid(grid):
        adj_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                char = grid[y][x]
                if grid[y][x].isnumeric() == False and char != ".":
                    if x > 0:
                        adj_grid[y][x - 1] = 1
                    if y > 0:
                        adj_grid[y - 1][x] = 1
                    if y < len(grid) - 1:
                        adj_grid[y + 1][x] = 1
                    if x < len(grid[0]) - 1:
                        adj_grid[y][x + 1] = 1
                    if x > 0 and y > 0:
                        adj_grid[y - 1][x - 1] = 1
                    if x > 0 and y < len(grid) - 1:
                        adj_grid[y + 1][x - 1] = 1
                    if x < len(grid[0]) and y < len(grid[0]):
                        adj_grid[y+1][x+1] = 1
                    if x < len(grid[0]) and y > 0:
                        adj_grid[y-1][x+1] = 1
        return adj_grid

    def solve2(path):
        file = open(path)
        lines = file.readlines()
        string = file.read()
        strippedlines = []
        splitlines = []
        split_char = " "

        for line in lines:
            stripped = line.strip()
            strippedlines.append(stripped)
            split = line.strip().split(split_char)
            splitlines.append(split)
        
        print(strippedlines)

        adj_grid = Solver.build_adjacent_grid(strippedlines)
        for line in adj_grid:
            print(line)

        result = 0

        for y, line in enumerate(strippedlines):
            line_nums = []
            current_num = ""
            is_valid = False
            for x, char in enumerate(line):
                # cases - numeric char already validated, numeric char not yet validated, non-numeric char
                if char.isnumeric() and adj_grid[y][x] == 1:
                    is_valid = True
                    current_num = current_num + char
                elif char.isnumeric():
                    current_num = current_num + char
                else:
                    if is_valid: 
                        print("adding num", current_num)
                        result += int(current_num)
                    current_num = ""
                    is_valid = False
            if is_valid: result += int(current_num)
            current_num = ""
            is_valid = False


    
        return result
    
    def is_valid(move, grid):
        y, x = move
        return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0])
    
    def get_nums(y, x, grid):
        nums = []
        moves = [(y - 1, x - 1), 
                 (y - 1, x), 
                 (y - 1, x + 1),
                 (y, x - 1),
                 (y, x),
                 (y, x + 1),
                 (y + 1, x - 1),
                 (y + 1, x),
                 (y + 1, x + 1)]
        visited = set()
        for move in moves:
            if not Solver.is_valid(move, grid) or move in visited or not grid[move[0]][move[1]].isnumeric():
                continue
            else:
                y, x = move
                visited.add(move)
                print("adding", grid[y][x])
                num = grid[y][x]
                x2 = x - 1
                # check back y
                while x2 >= 0 and grid[y][x2].isnumeric():
                    num = grid[y][x2] + num
                    visited.add((y, x2))
                    x2 = x2 - 1
                # check front y
                x3 = x + 1
                while x3 < len(grid[0]) and grid[y][x3].isnumeric():
                    num = num + grid[y][x3]
                    visited.add((y, x3))
                    x3 = x3 + 1
                print("appending num", num)
                nums.append(num)
        return nums
                    

    
    def solve(path):
        result = 0
        file = open(path)
        lines = file.readlines()
        string = file.read()
        strippedlines = []
        splitlines = []
        split_char = " "

        for line in lines:
            stripped = line.strip()
            strippedlines.append(stripped)
            split = line.strip().split(split_char)
            splitlines.append(split)
        
        print(strippedlines)
        gear_posns = []
        for y, line in enumerate(strippedlines):
            for x, char in enumerate(line):
                if char == "*":
                    gear_posns.append((y, x))
        
        for y, x in gear_posns:
            nums = Solver.get_nums(y, x, strippedlines)
            if len(nums) == 2: result += int(nums[1]) * int(nums[0])
        return result

            

                    





soln = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2023-solutions\\2023-12-03\\input\\DEMO.txt')
print(soln)

solndemo = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2023-solutions\\2023-12-03\\input\\DATA.txt')
print(solndemo)
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
        split_char = ";"

        for line in lines:
            stripped = line.strip()
            strippedlines.append(stripped)
            split = line.strip().split(split_char)
            splitlines.append(split)
        result = 0
        games = splitlines
        for id, game in enumerate(games):
            id2 = id + 1
            game_red, game_blue, game_green = 0, 0, 0
            max_red, max_blue, max_green = 0, 0, 0

            for round in game:
                round = round.split(",")
                for move in round:
                    if len(move.split(" ")) == 4:
                        fake, fake2, count, color = move.split(" ")
                    else:
                        fake, count, color = move.split(" ")
                    print(move, color, count)
                    count = int(count)
                    if color == "red":
                        max_red = max(max_red, count)
                    elif color == "green":
                        max_green = max(max_green, count)
                    elif color == "blue":
                        max_blue = max(max_blue, count)
            print(game, id)
            print(game_red, game_blue, game_green)
            result += max_red * max_blue * max_green
        return result
                
    
    

        ### start program here






soln = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2023-solutions\\2023-12-02\\input\\DEMO.txt')
print(soln)

#solndemo = Solver.solve('C:\\Users\\gleas\\Projects\\AdventOfCode\\2023-solutions\\2023-12-02\\input\\DATA.txt')
#print(solndemo)
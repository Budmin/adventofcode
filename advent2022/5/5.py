from pprint import pprint 
from parse import parse
import time

input = '''move 3 from 6 to 2
move 5 from 6 to 7
move 6 from 2 to 5
move 1 from 9 to 7
move 1 from 1 to 9
move 1 from 5 to 3
move 1 from 2 to 5
move 3 from 4 to 5
move 10 from 7 to 3
move 1 from 4 to 9
move 6 from 8 to 7
move 4 from 7 to 8
move 1 from 7 to 3
move 1 from 1 to 2
move 1 from 2 to 8
move 1 from 9 to 1
move 3 from 9 to 4
move 4 from 8 to 3
move 4 from 7 to 1
move 4 from 4 to 6
move 2 from 8 to 7
move 9 from 3 to 8
move 2 from 7 to 4
move 3 from 4 to 9
move 4 from 1 to 9
move 4 from 3 to 9
move 2 from 1 to 4
move 1 from 4 to 6
move 3 from 3 to 2
move 1 from 2 to 8
move 1 from 2 to 7
move 3 from 6 to 2
move 2 from 6 to 7
move 4 from 2 to 3
move 3 from 7 to 9
move 2 from 5 to 6
move 15 from 9 to 4
move 4 from 9 to 2
move 12 from 5 to 4
move 9 from 8 to 5
move 25 from 4 to 7
move 1 from 4 to 7
move 1 from 4 to 8
move 2 from 2 to 5
move 1 from 4 to 2
move 23 from 7 to 6
move 2 from 5 to 2
move 22 from 6 to 8
move 4 from 5 to 9
move 1 from 7 to 9
move 2 from 6 to 4
move 2 from 4 to 7
move 25 from 8 to 3
move 1 from 2 to 1
move 3 from 2 to 3
move 1 from 6 to 8
move 1 from 1 to 8
move 1 from 2 to 8
move 1 from 8 to 1
move 4 from 5 to 7
move 1 from 8 to 4
move 5 from 9 to 8
move 5 from 8 to 9
move 1 from 8 to 5
move 3 from 5 to 4
move 3 from 9 to 1
move 30 from 3 to 4
move 3 from 1 to 4
move 2 from 9 to 5
move 4 from 7 to 9
move 16 from 4 to 8
move 6 from 3 to 9
move 3 from 7 to 3
move 19 from 4 to 7
move 8 from 9 to 4
move 1 from 1 to 9
move 13 from 7 to 9
move 3 from 7 to 8
move 3 from 5 to 9
move 4 from 8 to 3
move 2 from 7 to 3
move 14 from 9 to 4
move 10 from 3 to 1
move 12 from 4 to 8
move 6 from 1 to 9
move 1 from 1 to 2
move 1 from 7 to 1
move 6 from 9 to 3
move 17 from 8 to 6
move 10 from 8 to 5
move 1 from 7 to 8
move 1 from 9 to 5
move 2 from 3 to 1
move 4 from 5 to 9
move 1 from 8 to 7
move 6 from 9 to 7
move 4 from 4 to 2
move 3 from 4 to 6
move 4 from 5 to 9
move 4 from 9 to 3
move 1 from 2 to 4
move 4 from 4 to 7
move 3 from 5 to 3
move 1 from 4 to 5
move 5 from 1 to 2
move 1 from 1 to 9
move 7 from 2 to 7
move 1 from 5 to 7
move 8 from 3 to 5
move 20 from 6 to 7
move 9 from 7 to 9
move 2 from 2 to 9
move 2 from 3 to 1
move 2 from 1 to 3
move 2 from 3 to 4
move 2 from 4 to 6
move 1 from 3 to 9
move 1 from 4 to 9
move 1 from 6 to 9
move 2 from 5 to 8
move 2 from 8 to 5
move 1 from 6 to 7
move 2 from 5 to 8
move 6 from 9 to 5
move 2 from 8 to 6
move 11 from 9 to 2
move 1 from 6 to 5
move 11 from 2 to 5
move 1 from 6 to 4
move 7 from 5 to 9
move 7 from 9 to 1
move 1 from 4 to 9
move 28 from 7 to 5
move 1 from 7 to 5
move 5 from 5 to 9
move 5 from 9 to 3
move 6 from 1 to 8
move 1 from 1 to 7
move 5 from 3 to 2
move 1 from 7 to 8
move 7 from 8 to 1
move 1 from 9 to 4
move 2 from 2 to 5
move 22 from 5 to 3
move 1 from 7 to 8
move 1 from 4 to 7
move 1 from 8 to 9
move 1 from 9 to 4
move 14 from 5 to 7
move 5 from 5 to 9
move 19 from 3 to 4
move 1 from 2 to 9
move 2 from 2 to 5
move 1 from 5 to 1
move 6 from 1 to 7
move 2 from 7 to 6
move 1 from 1 to 9
move 2 from 5 to 8
move 8 from 4 to 5
move 3 from 4 to 7
move 3 from 3 to 5
move 2 from 8 to 9
move 16 from 7 to 5
move 9 from 4 to 6
move 22 from 5 to 3
move 1 from 5 to 8
move 1 from 8 to 7
move 10 from 3 to 4
move 1 from 5 to 4
move 10 from 4 to 5
move 8 from 5 to 2
move 5 from 2 to 7
move 5 from 7 to 1
move 4 from 7 to 6
move 3 from 9 to 7
move 2 from 2 to 3
move 3 from 5 to 1
move 6 from 9 to 7
move 5 from 7 to 8
move 6 from 1 to 5
move 6 from 3 to 4
move 4 from 4 to 2
move 1 from 4 to 6
move 5 from 8 to 7
move 3 from 2 to 3
move 1 from 1 to 4
move 1 from 1 to 9
move 2 from 2 to 1
move 2 from 4 to 3
move 4 from 3 to 7
move 3 from 7 to 3
move 13 from 6 to 1
move 1 from 9 to 2
move 6 from 3 to 5
move 8 from 1 to 4
move 1 from 2 to 7
move 9 from 4 to 9
move 7 from 5 to 1
move 2 from 5 to 6
move 1 from 1 to 4
move 1 from 4 to 3
move 2 from 1 to 2
move 5 from 3 to 6
move 2 from 6 to 1
move 13 from 7 to 6
move 2 from 3 to 4
move 2 from 2 to 9
move 2 from 7 to 8
move 6 from 9 to 2
move 1 from 9 to 3
move 1 from 5 to 2
move 7 from 1 to 2
move 1 from 6 to 7
move 1 from 4 to 8
move 1 from 3 to 1
move 1 from 7 to 8
move 7 from 1 to 9
move 4 from 8 to 6
move 1 from 5 to 3
move 9 from 9 to 5
move 1 from 1 to 2
move 14 from 2 to 7
move 2 from 9 to 3
move 13 from 5 to 3
move 24 from 6 to 9
move 6 from 3 to 5
move 14 from 7 to 9
move 1 from 4 to 1
move 20 from 9 to 7
move 9 from 3 to 8
move 15 from 9 to 6
move 1 from 5 to 8
move 1 from 2 to 3
move 14 from 6 to 3
move 2 from 3 to 4
move 2 from 3 to 6
move 13 from 7 to 1
move 8 from 3 to 5
move 1 from 3 to 9
move 8 from 5 to 4
move 4 from 5 to 2
move 10 from 1 to 3
move 6 from 4 to 5
move 4 from 5 to 1
move 3 from 1 to 6
move 7 from 8 to 2
move 4 from 4 to 3
move 13 from 3 to 6
move 3 from 8 to 1
move 3 from 7 to 8
move 3 from 8 to 4
move 1 from 4 to 2
move 2 from 3 to 4
move 1 from 5 to 7
move 4 from 7 to 1
move 2 from 3 to 5
move 3 from 2 to 1
move 1 from 4 to 7
move 7 from 2 to 4
move 2 from 4 to 3
move 1 from 7 to 5
move 4 from 9 to 5
move 1 from 4 to 2
move 3 from 2 to 9
move 8 from 1 to 7
move 1 from 3 to 5
move 7 from 5 to 7
move 10 from 6 to 4
move 1 from 5 to 1
move 4 from 1 to 3
move 9 from 7 to 6
move 3 from 1 to 8
move 12 from 4 to 6
move 5 from 4 to 6
move 2 from 9 to 3
move 3 from 8 to 7
move 1 from 1 to 3
move 3 from 7 to 8
move 5 from 7 to 5
move 1 from 7 to 5
move 2 from 3 to 1
move 2 from 8 to 7
move 3 from 5 to 1
move 1 from 9 to 7
move 1 from 8 to 3
move 4 from 7 to 8
move 4 from 5 to 9
move 4 from 1 to 7
move 3 from 8 to 6
move 1 from 8 to 1
move 1 from 7 to 1
move 1 from 5 to 8
move 1 from 8 to 7
move 7 from 3 to 1
move 3 from 9 to 1
move 1 from 9 to 3
move 28 from 6 to 3
move 3 from 7 to 8
move 2 from 8 to 2
move 1 from 2 to 7
move 2 from 6 to 1
move 18 from 3 to 9
move 5 from 3 to 4
move 2 from 7 to 4
move 2 from 1 to 8
move 1 from 2 to 6
move 7 from 6 to 4
move 4 from 4 to 3
move 3 from 8 to 1
move 4 from 9 to 8
move 1 from 4 to 8
move 9 from 1 to 6
move 5 from 1 to 3
move 4 from 6 to 7
move 7 from 6 to 3
move 5 from 8 to 1
move 12 from 3 to 6
move 7 from 6 to 4
move 4 from 3 to 5
move 5 from 6 to 7
move 12 from 4 to 3
move 6 from 1 to 4
move 4 from 4 to 2
move 14 from 9 to 8
move 17 from 3 to 2
move 5 from 4 to 9
move 1 from 9 to 6
move 5 from 2 to 1
move 1 from 9 to 8
move 5 from 1 to 6
move 2 from 2 to 6
move 12 from 2 to 4
move 6 from 7 to 2
move 3 from 7 to 6
move 3 from 9 to 8
move 5 from 4 to 7
move 4 from 2 to 6
move 3 from 6 to 8
move 5 from 8 to 2
move 7 from 6 to 8
move 1 from 7 to 3
move 6 from 4 to 3
move 1 from 8 to 1
move 1 from 5 to 7
move 2 from 6 to 8
move 13 from 8 to 2
move 3 from 5 to 4
move 1 from 1 to 2
move 3 from 6 to 2
move 1 from 1 to 4
move 4 from 4 to 8
move 8 from 3 to 1
move 2 from 4 to 8
move 15 from 2 to 4
move 16 from 8 to 3
move 1 from 8 to 6
move 1 from 7 to 2
move 8 from 1 to 2
move 1 from 6 to 8
move 6 from 3 to 1
move 3 from 3 to 8
move 6 from 3 to 1
move 6 from 2 to 9
move 2 from 1 to 4
move 1 from 8 to 5
move 8 from 2 to 9
move 8 from 1 to 4
move 3 from 8 to 6
move 21 from 4 to 7
move 1 from 9 to 7
move 2 from 6 to 8
move 1 from 5 to 1
move 1 from 3 to 9
move 8 from 9 to 4
move 1 from 1 to 7
move 1 from 1 to 4
move 1 from 6 to 8
move 1 from 9 to 3
move 2 from 9 to 5
move 2 from 5 to 3
move 1 from 9 to 4
move 3 from 8 to 2
move 1 from 1 to 4
move 4 from 4 to 9
move 3 from 3 to 2
move 5 from 9 to 1
move 17 from 7 to 1
move 1 from 9 to 1
move 2 from 2 to 4
move 1 from 4 to 2
move 8 from 2 to 9
move 5 from 4 to 5
move 6 from 4 to 8
move 20 from 1 to 6
move 2 from 9 to 8
move 1 from 2 to 9
move 2 from 8 to 7
move 8 from 7 to 8
move 4 from 5 to 9
move 14 from 8 to 7
move 1 from 5 to 7
move 7 from 9 to 1
move 3 from 6 to 4
move 3 from 9 to 7
move 12 from 6 to 7
move 22 from 7 to 9
move 2 from 2 to 5
move 10 from 1 to 7
move 1 from 4 to 1
move 2 from 6 to 1
move 1 from 1 to 3
move 2 from 4 to 8
move 2 from 8 to 6
move 1 from 3 to 8
move 1 from 4 to 1
move 2 from 5 to 3
move 1 from 8 to 4
move 2 from 3 to 7
move 19 from 9 to 7
move 1 from 1 to 4
move 2 from 9 to 1
move 2 from 1 to 6
move 1 from 6 to 5
move 42 from 7 to 8
move 1 from 7 to 6
move 2 from 4 to 8
move 7 from 6 to 8
move 2 from 1 to 5
move 2 from 9 to 5
move 14 from 8 to 3
move 22 from 8 to 2
move 3 from 5 to 6
move 10 from 8 to 6
move 5 from 8 to 9
move 12 from 6 to 7
move 2 from 5 to 1
move 5 from 3 to 2
move 7 from 3 to 5
move 2 from 5 to 1
move 2 from 3 to 7
move 4 from 1 to 2
move 1 from 5 to 7
move 1 from 5 to 4
move 1 from 6 to 2
move 1 from 9 to 2
move 9 from 7 to 3
move 1 from 4 to 1
move 3 from 7 to 5
move 4 from 3 to 2
move 5 from 2 to 3
move 2 from 5 to 2
move 34 from 2 to 9
move 1 from 1 to 5
move 15 from 9 to 3
move 2 from 3 to 2
move 1 from 5 to 4
move 7 from 3 to 8
move 3 from 9 to 2
move 6 from 9 to 4
move 5 from 9 to 3
move 4 from 4 to 6
move 1 from 6 to 8
move 1 from 3 to 5
move 6 from 3 to 2
move 1 from 4 to 9
move 2 from 4 to 2
move 4 from 5 to 8
move 1 from 5 to 6
move 1 from 7 to 6
move 1 from 9 to 6
move 1 from 7 to 2
move 12 from 8 to 7
move 2 from 7 to 3
move 4 from 6 to 9
move 7 from 9 to 4
move 9 from 3 to 9
move 11 from 7 to 4
move 3 from 9 to 6
move 1 from 4 to 1
move 15 from 4 to 3
move 2 from 4 to 1
move 3 from 1 to 4
move 17 from 3 to 7
move 4 from 3 to 7
move 7 from 9 to 2
move 3 from 4 to 1
move 4 from 6 to 9
move 1 from 9 to 6
move 1 from 3 to 1
move 5 from 7 to 9
move 8 from 9 to 4
move 1 from 1 to 6
move 6 from 4 to 9
move 4 from 2 to 3
move 1 from 4 to 3
move 1 from 4 to 9
move 1 from 1 to 7
move 1 from 7 to 9
move 3 from 6 to 2
move 9 from 2 to 3
move 1 from 9 to 4
move 1 from 1 to 5
move 12 from 7 to 6
move 4 from 9 to 8'''

#                     [Q]     [P] [P]
#                 [G] [V] [S] [Z] [F]
#             [W] [V] [F] [Z] [W] [Q]
#         [V] [T] [N] [J] [W] [B] [W]
#     [Z] [L] [V] [B] [C] [R] [N] [M]
# [C] [W] [R] [H] [H] [P] [T] [M] [B]
# [Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
# [B] [R] [B] [C] [D] [H] [D] [C] [N]
#  1   2   3   4   5   6   7   8   9 

stacks = {
  "1": ["C", "Q", "B"],
  "2": ["Z", "W", "Q", "R"],
  "3": ["V", "L", "R", "M", "B"],
  "4": ["W", "T", "V", "H", "Z", "C"],
  "5": ["G", "V", "N", "B", "H", "Z", "D"],
  "6": ["Q", "V", "F", "J", "C", "P", "N", "H"],
  "7": ["S", "Z", "W", "R", "T", "G", "D"],
  "8": ["P", "Z", "W", "B", "N", "M", "G", "C"],
  "9": ["P", "F", "Q", "W", "M", "B", "J", "N"]
}


# test data
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# stacks = {
#   "1": ["N", "Z"],
#   "2": ["D", "C", "M"],
#   "3": ["P"]
# }

# input = '''move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''


def main():
  steps = [ parse("move {} from {} to {}", step)   for step in input.split("\n")]

  for step in steps:


    move_count = int(step[0])
    move_from = step[1]
    move_to = step[2]


    # get stack
    move_stack = stacks[move_from][:move_count]

    # this is for part 1
    # comment the reverse out for part 2
    # move_stack.reverse()

    
    # update the old stack
    stacks[move_from] = stacks[move_from][move_count:]

    # move to new stack
    stacks[move_to] = move_stack + stacks[move_to]




  for key in stacks:
    print(stacks[key][0], end="")

  print("")





if __name__ == "__main__":
  main()
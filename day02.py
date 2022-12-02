f = open("day02_input.txt")
input = f.readlines()

shape_score = {'Rr': 1, 'Rp': 2, 'Rs': 3,
               'Pr': 1, 'Pp': 2, 'Ps': 3,
               'Sr': 1, 'Sp': 2, 'Ss': 3
               }

result_score ={'Rr': 3, 'Rp': 6, 'Rs': 0,
               'Pr': 0, 'Pp': 3, 'Ps': 6,
               'Sr': 6, 'Sp': 0, 'Ss': 3
               }

key={'A': 'R', 'B': 'P', 'C': 'S',
     'X': 'r', 'Y': 'p', 'Z': 's'}
score = 0
for l in input:
    game = key[l[0]]+key[l[2]]
    score += shape_score[game] + result_score[game]

print("Part One:",score)

#################

key = {'A X': 'Rs', 'B X': 'Pr', 'C X': 'Sp',
       'A Y': 'Rr', 'B Y': 'Pp', 'C Y': 'Ss',
       'A Z': 'Rp', 'B Z': 'Ps', 'C Z': 'Sr'
       }

score = 0
for l in input:
    game = key[l[0:3]]
    score += shape_score[game] + result_score[game]

print("Part Two:",score)
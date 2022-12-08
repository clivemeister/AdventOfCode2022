# AdventOfCode 2022 day 5
f = open("day05_input.txt")
input = f.readlines()

from collections import defaultdict
stacks = defaultdict(list)

# read the stacks
maxheight=0
stackcount=0
for line in input:
    line = line.strip('\n')
    
    #check if we've got to the end of the stacks in the input file
    if len(line)==0:
        break

    if line.find('[') != -1:
        # found another row with elements of the stack in it
        maxheight += 1
        i=0
        while i<len(line):
            if line[i] == '[':
                stack_idx = int(1 + i/4)
                stacks[stack_idx].insert(0,line[i+1])
                stackcount = max(stackcount,stack_idx)
                i += 3
            else:
                i += 1

# save a copy for Part Two
import copy
savedstacks = copy.deepcopy(stacks)

# now process the moving instructions
import re
for i in range(maxheight+2,len(input)):
    vals = re.findall(r'\d+', input[i])
    num = int(vals[0])
    src = int(vals[1])
    tgt = int(vals[2])
    for j in range(0,num):
        stacks[tgt].append( stacks[src].pop() )

def topblocks(stacks):
    topblocks=''
    for i in range(1,stackcount+1):
        topblocks+=stacks[i].pop()
    return topblocks

print("First part key:",topblocks(stacks))

#######################################
# Now do part 2, using saved deepcopy of stacks 
# now process the moving instructions

for i in range(maxheight+2,len(input)):
    vals = re.findall(r'\d+', input[i])
    num = int(vals[0])
    src = int(vals[1])
    tgt = int(vals[2])
    savedstacks[tgt].extend( savedstacks[src][-num:] )   # use 'extend' to just append elements of one list to another
    savedstacks[src] = savedstacks[src][:-num]

print("Second part key:",topblocks(savedstacks))

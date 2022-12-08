f = open("day04_input.txt")
input = f.readlines()

import re
s1_start=[]
s1_end=[]
s2_start=[]
s2_end=[]
for i,line in enumerate(input):
    line = line.strip('\n')
    sections = re.findall(r'\d+-\d+',line)
    s1 = re.findall(r'\d+',sections[0])
    s2 = re.findall(r'\d+',sections[1])
    s1_start.append(int(s1[0]))
    s1_end.append(int(s1[1]))
    s2_start.append(int(s2[0]))
    s2_end.append(int(s2[1]))


contained_count = 0
for i in range(len(s1_start)):
    if s1_start[i]<s2_start[i]:
        if s1_end[i] >= s2_end[i]:
            contained_count += 1
    elif s1_start[i] == s2_start[i]:
        contained_count += 1
    else:
        if s2_end[i] >= s1_end[i]:
            contained_count += 1

print("First part count:", contained_count)

############################################

overlap_count = 0
for i in range(len(s1_start)):
    if s1_start[i]>s2_end[i] or s1_end[i]<s2_start[i]:
        #print("no overlap")
        pass
    else:
        overlap_count += 1
       
print("Second part count:",overlap_count)
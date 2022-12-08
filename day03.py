f = open("day03_input.txt")
input = f.readlines()

def buildScore():
    score=dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i,c in enumerate(alphabet):
        score[c]=i+1
        score[c.upper()]=i+27
    return score

score=buildScore()

tot=0
for l in input:
    length = len(l)
    c1 = set(l[0:int(length/2)])
    c2 = set(l[int(length/2):length])
    for s in c1.intersection(c2):
        tot+=score[s]

print("First part:",tot)

tot=0
for i in range(0,len(input),3):
    print(i)
    r1 = set(input[i].strip())
    r2 = set(input[i+1].strip())
    r3 = set(input[i+2].strip())
    c = r1.intersection(r2).intersection(r3)
    for s in c:
        tot+=score[s]
 
print("Second part:",tot)


f = open("day06_input.txt")
input = f.readlines()

if len(input)>1:
    print("Expecting only a single line, but read",len(input))
    exit(4)

sig = input[0]
for i in range(4,len(sig)+1):
    if len(set(sig[i-4:i])) == 4:
        print("Found start-of-packet ending at ",i)
        break

# Part Two
for i in range(14,len(sig)+1):
    if len(set(sig[i-14:i])) == 14:
        print("Found start-of-message ending at ",i)
        break
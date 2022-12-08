f = open("day07_test.txt")
input = f.readlines()


def getpath(lst):
    path = ''
    for item in lst:
        path += '/'+item
    return path

if input[0].strip(' \n') != '$ cd /':
    print("Unexpected first line - ",input[0])
    exit(-1)

current_path = ['root']
current_dir = getpath(current_path)
dirsize = {current_dir: 0}
subdirs = {current_dir: []}

i = 1  
while i<len(input):
    line = input[i].strip(' \n')
    print(line)
    if line=="$ ls":
        i += 1
        while i<len(input):
        
            words = input[i].strip(' \n').split()
        
            if words[1] =='cd':
                break  #come to the end of this dir listing, so break out

            if words[0].isdigit():
                dirsize[current_dir] += int(words[0])
            elif words[0] == 'dir':
                subdirs[current_dir].append(words[1])
            elif words[0] != '$':
                print(f"unexpected line {i}: {input[i]}")

            i += 1
    elif line=="$ cd ..":
        print("Popping from path:", current_path)
        current_path.pop()
        i += 1
    else:
        words = line.split()
        next_dir = words[2]
        current_path.append(next_dir)
        current_dir = getpath(current_path)
        print("into new subdir",current_dir)
        if current_dir in dirsize:
            print("unexpectedly already have this directory:", current_dir)
        else:
            dirsize[current_dir] = 0
            subdirs[current_dir] = []

        i += 1

def dir_size_with_subdirs(thisdir):
    size = dirsize[thisdir]
    for subdir in subdirs[thisdir]:
        size += dir_size_with_subdirs(subdir)
    return size

tot = 0
for dir in dirsize:
    print("sizing directory",dir)
    size = dir_size_with_subdirs(dir)
    print("Size with subdirs:",dir,size)
    if size<=100000:
        tot += size

print("\nTotal of all directories with size at most 100000:",tot)
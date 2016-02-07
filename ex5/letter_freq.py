import sys

# check arguments
if len(sys.argv) != 2:
    print("usage:")
    print("python letter_freq.py input.txt")
    exit(0)

# open file
f = open(sys.argv[1])
# read all lines
a = f.read()
f.close()

# the alphabet
alpha = 'abcdefghijklmnopqrstuvwzyz'

# add to dictionary
count = {}
for x in a:
    # count only alphabets
    if x.lower() in alpha:
        if x in count:
            count[x.lower()] += 1
        else:
            count[x.lower()] = 1
        
#print(count)
#print(len(a))

# get the maximum count
maxCount = max(count.values())

# print graph
for x in alpha:
    if x in count:
        nBars = count[x]*70//maxCount
        print("%s: %s" % (x, nBars*'#'))
    else:
        print("%s: " % (x,))




import turtle as t
import sys

# check arguments
if len(sys.argv) != 2:
    print("usage:")
    print("python showgrafix.py input.txt")
    exit(0)

# open file
f = open(sys.argv[1])
# read all lines
lines = f.readlines()
f.close()

linenum = 1
# go through each line
for line in lines:
    if line[0].strip() == '#':
        # skip
        pass
    else:
        c = line.strip().split()
        if len(c) == 4:
            x1, y1, x2, y2 = float(c[0]), float(c[1]), float(c[2]), float(c[3]) 
            t.pu()
            t.setpos(x1, y1)
            t.pd()
            t.setpos(x2, y2)
            t.pu()
        elif len(c) == 0:
            pass
        else:
            print("Error in line %d!", linenum)
            print(line)
            exit(0)
    # keep track of line numbers
    linenum += 1

t.hideturtle()
t.mainloop()


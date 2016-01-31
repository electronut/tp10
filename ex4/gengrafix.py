import math

def genCircle(x, y, R, N):
    """generates points for a circle of radius R with 
    N segments, centered at x, y
    """
    coords = []
    theta = 2*math.pi/N
    for i in range(N):
        coords.append((R*math.cos(i*theta) + x, 
                       R*math.sin(i*theta) + y,
                       R*math.cos((i+1)*theta) + x, 
                       R*math.sin((i+1)*theta) + y))
    return coords

def writeGeom(f, coords):
    """writes supplied coords to file stream"""
    for coord in coords:
        f.write("%f %f %f %f\n" % (coord[0], coord[1], coord[2], coord[3]))
        
f = open('geom.txt', 'w')
f.write("# gem.txt\n# Custom geometry!\n")
c1 = genCircle(0, 0, 200, 25)
writeGeom(f, c1) 
c2 = genCircle(80, 50, 40, 25)
writeGeom(f, c2) 
c3 = genCircle(-80, 50, 40, 25)
writeGeom(f, c3) 
c4 = genCircle(0, -20, 20, 25)
writeGeom(f, c4) 

# line
coords = [(-40, -80, 40, -80)]
writeGeom(f, coords) 

f.close()

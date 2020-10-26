from scipy.spatial import ConvexHull
import numpy as np

def point_in_hull(point, hull, tolerance=1e-12):
    return all(
        (np.dot(eq[:-1], point) + eq[-1] <= tolerance)
        for eq in hull.equations)

def point_in_line(line, point):
    x0 = line[0][0]
    y0 = line[0][1]
    x1 = line[1][0]
    y1 = line[1][1]

    m = (y0 - y1) / (x1 - x0)
    b = y0 - m * x0

    x = point[0]
    y = point[1]

    return y == m * x + b

# Number of queries
T = int(input())

for i in range(T):
    N = int(input())
    p1 = [] # Positive points
    p2 = [] # Negative points

    for j in range(N):
        point = [float(x) for x in input().split(" ")]

        if point[-1] == 1:
            p1.append(point[0:2])

        else:
            p2.append(point[0:2])

    if len(p1) > 2:
        p1 = np.array(p1)

        hull = ConvexHull(p1)
        print(hull.equations)

        for point in p2:
            if point_in_hull(point, hull): # Point is inside convex hull
                print("NO")

        else:
            print("YES")

    else:
        print("NO")

        

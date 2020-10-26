def ccw(A,B,C):
    return (C[1] -A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# Number of queries
T = int(input())

for i in range(T):
    N = int(input())

    points = {
        -1: [],
        1: []
    }

    for j in range(N):
        point = [float(x) for x in input().split(" ")]
        points[point[-1]] = point[0:2]
    print(points)
    for j in range(len(points[1]) - 1):
        for k in range(len(points[-1]) - 1):
            p1 = points[1][j]
            p2 = points[1][j + 1]
            print("P1 is ", p1)

            n1 = points[-1][k]
            n2 = points[-1][k + 1]

            if intersect(p1, p2, n1, n2):
                print("NO")
                break

    print("YES")

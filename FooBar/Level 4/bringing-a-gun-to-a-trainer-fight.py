class Point:
    """Class that represents a two-dimensional point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x, self.y}"

    def mirror(self, i, j, w, h):
        x = self.x if i % 2 == 0 else w - self.x
        y = self.y if j % 2 == 0 else h - self.y

        x += i * w
        y += j * h

        return Point(x, y)

class Vector:
    """Class that represents a two-dimensional vector"""
    def __init__(self, p1, p2): 
        if type(p1) == Point and type(p2) == Point:
            self.u = p2.x - p1.x
            self.v = p2.y - p1.y

        else:
            self.u = p1
            self.v = p2

    def __str__(self):
        return f"{self.u, self.v}"
    
    def norm(self):
        """Calculates the vector's norm"""

        return (self.u ** 2 + self.v ** 2) ** 0.5

    def normalized(self):
        if self.norm() == 0:
            return Vector(0, 0)

        return Vector(self.u / self.norm(), self.v / self.norm())

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"<{self.p1}, {self.p2}>"

    def vector(self):
        return Vector(self.p1, self.p2)

    def length(self):
        """Calculates the segment's length"""

        return self.vector().norm()

    def contains(self, p):
        """Check if the segment contains a point"""

        x1, x2, x3 = self.p1.x, self.p2.x, p.x
        y1, y2, y3 = self.p1.y, self.p2.y, p.y

        if (x3 == x2):
            return y1 <= y3 <= y2

        slope = (y2 - y1) / (x2 - x1)
        
        pt3_on = (y3 - y1) == slope * (x3 - x1) 
        pt3_between = (min(x1, x2) <= x3 <= max(x1, x2)) and (min(y1, y2) <= y3 <= max(y1, y2))

        return pt3_on and pt3_between

def solution(dimensions, your_position, trainer_position, distance):
    result = set()  # Set containing the directions in which the gun may be shot    
    feasible = True
    i = 1

    # Convert the positions into points
    your_position = Point(your_position[0], your_position[1])
    trainer_position = Point(trainer_position[0], trainer_position[1])

    while feasible:
        feasible = False
        offsets = set()

        for j in range(-i, i + 1):
            offsets.add((j, i))
            offsets.add((j, -i))
            offsets.add((i, j))
            offsets.add((-i, j))

        for offset in offsets:
            new_trainer_position = trainer_position.mirror(offset[0], offset[1], dimensions[0], dimensions[1])
            new_your_position = your_position.mirror(offset[0], offset[1], dimensions[0], dimensions[1])

            s = Segment(your_position, new_trainer_position)

            if s.length() <= distance and not s.contains(new_your_position):
                feasible = True
                v = s.vector().normalized()
                result.add(v)
                print(v)

        i += 1

    return len(result)

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))

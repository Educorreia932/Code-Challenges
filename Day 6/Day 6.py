# Structure similar to a tree
class Orbit(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, object, sattelite):
        if (self.data == object):
            self.children.append(sattelite)
            
            return True
        
        else:
            for child in self.children:
                if (child.add(object, sattelite)):
                    return True
                
        return False    
    
    def depth(self, object, count = 0):        
        if self.data == object:
            return count
        
        for child in self.children:
            depth = child.depth(object, count + 1)
            
            if (depth != None):
                return depth
    
    def count(self, depth = 0):      
        sum = len(self.children)   
        
        if (depth > 1):
            sum += depth - 1
        
        for child in self.children:            
            sum += child.count(depth + 1)
            
        return sum
    
    def print(self):
        print(self.data)
        
        if self.children == []:
            return
            
        else:
            for child in self.children:
                child.print()
                
    def find(self, data):
        if self.data == data:
            return self
        
        for child in self.children:
            result = child.find(data)
            
            if result != None:
                return result        
          
input = open("Day 6 - Input.txt", "r").read().split("\n")

orbits = Orbit("Root")

for object in input:
    objects = object.split(")")
    
    search = orbits.find(objects[1])

    if search != None:
        if orbits.add(objects[0], search) == False:
            orbits.add("Root", search)
            orbits.add(objects[0], search)   

    elif orbits.add(objects[0], Orbit(objects[1])) == False:
        orbits.add("Root", Orbit(objects[0]))
        orbits.add(objects[0], Orbit(objects[1]))

result = 0

for child in orbits.children:
    if child.data == "COM":
        result = child.count()
        
        break

print(result)
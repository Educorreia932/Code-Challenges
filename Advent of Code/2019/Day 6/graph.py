import pyyed

file = open("Day 6 - Input.txt", "r").read().split("\n")

g = pyyed.Graph()

for line in file:
    objects= line.split(")")
    
    object1 = objects[0]
    object2 = objects[1]
    
    try:
        g.add_node(object1)
        g.add_node(object2)
        
    except RuntimeWarning:
        pass
    
    g.add_edge(object1, object2)
    
output = open("Orbits.graphml", 'w')
output.write(g.get_graph())
output.close()

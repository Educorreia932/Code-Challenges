from collections import defaultdict
import copy

# This class represents a directed graph using adjacency list representation

paths = []

class Graph:
    def __init__(self, vertices):
        # Number of vertices
        self.V = vertices

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def allPathsUtil(self, u, d, visited, path):
        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print current path[]
        if u == d:
            global paths
            paths.append(set(path))

        else: 
            # If current vertex is not destination 
            # Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i] == False: 
                    self.allPathsUtil(i, d, visited, path) 
                    
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False

    # Prints all paths from 's' to 'd' 
    def allPaths(self, s, d): 
        # Mark all the vertices as not visited 
        visited = [False] * (self.V) 

        # Create an array to store paths 
        path = list()

        # Call the recursive helper function to print all paths 
        self.allPathsUtil(s, d, visited, path)

N, M = (int(x) for x in input().split(" "))

g = Graph(N) 

for i in range(M):
    A_i, B_i = (int(x) for x in input().split(" "))

    g.addEdge(A_i, B_i) 
    g.addEdge(B_i, A_i) 

Q = int(input())

for i in range(Q):
    F_i, S_i = (int(x) for x in input().split(" "))

    paths = []
    g.allPaths(F_i, S_i)

    common = set.intersection(*paths)

    print(len(common))


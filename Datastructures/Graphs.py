class Queue(object):

    def __init__(self):
        self.myqueue = []
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def add(self, item):
            self.myqueue.append(item)
            self.size +=1

    def remove(self):
        if self.size <= 0:
            print('Queue Underflow!')
            return -1
        else:
            self.size -=1
            return self.myqueue.pop(0)

    def peek(self):
        if self.size <= 0:
            print('Queue Underflow!')
            return -1
        else:
            return self.myqueue[0]

    def mysize(self):
        return self.size

class Vertex:
    def __init__(self,item):
        self.id = item
        self.neighbours = []
        self.inDegree = 0 #number of edges leading to the vertex


    def addNeighbour(self,neighbour):
        self.neighbours.append(neighbour)

    def getNeighbours(self):
        return self.neighbours

class Graph:
    def __init__(self):
        self.vertexCount = 0
        self.vertexInfo = {}

    #iteration
    def __iter__(self):
        return iter(self.vertexInfo.values())

    def addVertex(self,node):
        self.vertexCount += 1
        newVertex = Vertex(node)
        self.vertexInfo[node] = newVertex
        return newVertex

    def addEdge(self,frm,to):
        #Add vertex
        if frm not in self.vertexInfo:
            fromVertex = self.addVertex(frm)
        else:
            fromVertex = self.vertexInfo[frm]
        if to not in self.vertexInfo:
            toVertex = self.addVertex(to)
        else:
            toVertex = self.vertexInfo[to]
        #Add neighbour for frm vertex
        fromVertex.addNeighbour(toVertex)
        #Increment inDegree for to vertex
        toVertex.inDegree += 1

    def getVertices(self):
        return self.vertexInfo.keys()

    def getVerticesCount(self):
        return self.vertexCount

    def getEdges(self):
        edges = []
        for v in self:
            for w in v.getNeighbours():
                edges.append([v.id,w.id])
        return edges

G = Graph()
G.addEdge('A', 'B')
# G.addEdge('A', 'C')
# G.addEdge('A', 'D')
# G.addEdge('B', 'D')
# G.addEdge('B', 'C')
# print("#Vertices: ", G.getVerticesCount())
# print("All vertices: ", G.getVertices())
# print("All edges: ", G.getEdges())
print G.vertexInfo




'''
Use DFS find all path between two edges.
REFERENCE:
1. http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
2. https://www.cs.berkeley.edu/~vazirani/algorithms/chap4.pdf
NOTES:
1. Depth-first search makes deep incursions into a graph, retreating
   only when it runs out of new nodes to visit.
2. DFS can end up taking a long and convoluted route to a vertex
   that is actually very close by.
'''

'''
Time complexity is O(|V|), #nodes.
Space complexity in a recursive implementation is O(h) [worst case], where h is the maximal depth of the graph
'''

# #Depth First Traversal
# def DFT(graph,ConnectedNodes,end,visited,path):
# 	for ConnectedNode in ConnectedNodes:
# 		if ConnectedNode not in visited:
# 			#Append current node to visited
# 			visited.append(ConnectedNode)
# 			#Append current node to path
# 			path.append(ConnectedNode)
# 			#Found path!
# 			if ConnectedNode == end:
# 				yield path
# 			else:
#                 print "Hello"
# 				#continue
# 				#yield from DFT(graph,graph[ConnectedNode],end,visited,path)
# 			#pop current node from visited
# 			visited.pop()
# 			#pop current node from path
# 			path.pop()
#
#
# #Adjacency list
# graph = {'A': ['B', 'C'],
#          'B': ['A', 'D', 'E'],
#          'C': ['A', 'F'],
#          'D': ['B'],
#          'E': ['B', 'F'],
#          'F': ['C', 'E']}
#
# start = 'A'
# end  = 'F'
#
# for path in DFT(graph,graph[start],end,[start],[start]):
# 	print("->".join(path))


'''
Use BFS find all path between two edges.
REFERENCE:
1. http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
2. https://www.cs.berkeley.edu/~vazirani/algorithms/chap4.pdf
NOTES:
1. Breadth-first search visits vertices in increasing order
   of their distance from the starting point.
2. Breadth-first search always provides the shortest path between
   two connected vertices
3. Breadth-first search is a broader, shallower search, rather like the
   propagation of a wave upon water.
4. Queue is used for implementation
'''

'''
Time complexity is O(|V|) where |V| is the number of nodes, you need to traverse all nodes.
Space complexity is O(|V|) since at worst case you need to hold all nodes in the queue.
'''

def BFT(graph,start,end):
    q = Queue()
    #Store node and path
    q.add([start,start])
    #Keep track of visited nodes
    visited = []
    while not q.isEmpty():
        #get node and path from the queue
        nextNode,path = q.remove()
        #Found path!
        if nextNode == end:
            yield path
        else:
            #Visit all the edges of nextNone
            visited.append(nextNode)
            for node in graph[nextNode]:
                #node has been visited?
                if node not in visited:
                    #Store node and path
                    q.add([node,path+node])
                    print q.myqueue


#Adjacency list
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

start = 'A'
end  = 'F'
for path in BFT(graph,start,end):
    print("->".join(path))



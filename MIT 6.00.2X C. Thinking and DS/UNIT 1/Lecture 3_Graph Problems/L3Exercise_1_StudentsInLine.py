# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:38:40 2020

@author: LIGen
"""

# Consider our representation of permutations of students 
# in a line from Exercise 1. (The teacher only swaps the positions of
# two students that are next to each other in line.) 
# Let's consider a line of three students, Alice, Bob, and Carol 
# (denoted A, B, and C). Using the Graph class created in the lecture, 
# we can create a graph with the design chosen in Exercise 1: 
    # vertices represent permutations of the students in line; 
    # edges connect two permutations if one can be made into 
    # the other by swapping two adjacent students.



# =============================================================================
# Hint: How to get started?
# Write your code in terms of the nodes list from the code above. 
# For each node, think about what permutation is allowed. 
# A permutation of a set is a rearrangement of the elements in that set. 
# In this problem, you are only adding edges between nodes 
# whose permutations are between elements in the set beside each other . 
# For example, an acceptable permutation (edge) is 
# between "ABC" and "ACB" but not between "ABC" and "CAB".    
# =============================================================================


     
# Use the Classes Definition from the lecture:
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
# The reason why we set a "class" for 'Nodes', rather than just
# use 'string' to represent it, was to leave open the 
# possibility of having some date with more complicated kind of
# node that has properties other than its name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
# The key design decision here was to allow for the possibility
# of edges having directions.
               
class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        # Make sure the node doesn't repeat itself
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        # Make sure the nodes you gonna connect by this new edge
        # are in your graph
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    # To give the "dests" which are connecting to the "node"(src)
    def hasNode(self, node):
        return node in self.edges
    # Check whether an edge has a specific node
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
                # 'result' is a string
        return result[:-1] #omit final newline

class Graph(Digraph):
# Notice: consider why is Graph a subclass of Digraph
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        # the "Edge" here is a "class", but we 
        # reverse the dest and src
        Digraph.addEdge(self, rev)
        
        
        
# We construct our graph by first adding the following nodes:

    
# My Answer
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

def buildStuGraph(graphType):
    g = Graph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))        
    g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
    g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
    g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA'))) 
    g.addEdge(Edge(g.getNode('CBA'), g.getNode('BCA')))       
    return g
        
GStu = buildStuGraph(Graph)



# =============================================================================
# # Sample Answer
# g = Graph
# for n in nodes:
#     g.addNode(n)
# g.addEdge(Edge(nodes[0], nodes[1]))
# g.addEdge(Edge(nodes[0], nodes[2]))
# g.addEdge(Edge(nodes[1], nodes[4]))
# g.addEdge(Edge(nodes[2], nodes[3]))
# g.addEdge(Edge(nodes[3], nodes[5]))
# g.addEdge(Edge(nodes[4], nodes[5]))
# 
# # or some variation on this. Obviously, in a Graph,
# # g.addEdge(Edge(nodes[0], nodes[1])) functions just as well as
# # g.addEdge(Edge(nodes[1], nodes[0])).
# =============================================================================


        
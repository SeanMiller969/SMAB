#This is my node class, to be used in graphs or trees
import heapq

class Node:
    '''A regular node class'''
    #Constructors
    def __init__(self, value, children) -> None:
        self.value = value
        self.children = children
        self.visited = False
    def __init__(self) -> None:
        self.value = 99999999
        self.children = []
        self.visited = False

#These are template search functions, they will iterate through an entire
def dfs(root):
    if len(root.children) == 0:
        return root.value
    root.visited = True
    for node in root.children:
        if node.visited == False:
            dfs(node)
        
def bfs(root):
    if len(root.children) == 0:
        return root.value
    root.visited = True
    bfsQ = []
    bfsQ.append(root)
    while len(bfsQ) != 0:
        #pop(0) removes from front of list
        node = bfsQ.pop(0)
        node.visited = True
        for n in node.children():
            if n.visited == False:
                bfsQ.append(n)


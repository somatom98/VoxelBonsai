class DataTree:
    def __init__(self, firstNode):
        self.nodes = {}
        self.nodes[firstNode] = []
    
    def addEdge(self, node, nodeToAdd):
        if self.nodes.get(node) == None:
            return
        self.nodes[node].append(nodeToAdd)
        self.nodes[nodeToAdd] = []        

    def hasNext(self, node):
        return self.nodes.get(node) != None and len(self.nodes[node]) > 0
    
    def findNextNodes(self, node):
        return self.nodes[node]

    def change(self, oldNode, newNode):
        if self.nodes.get(oldNode) == None:
            return
        self.nodes[oldNode] = newNode
        for node in self.nodes.keys():
            for childNode in self.nodes[node]:
                if childNode == oldNode:
                    self.nodes[node].remove(childNode)
                    self.nodes[node].append(newNode)
                    return

    def incrementAllNodes(self, increment):
        incrementedNodes = {}
        for node in self.nodes.keys():
            newNode = node+increment
            incrementedNodes[newNode] = []
            for childNode in self.nodes[node]:
                newChildNode = childNode + increment
                incrementedNodes[newNode].append(newChildNode)
        self.nodes = incrementedNodes
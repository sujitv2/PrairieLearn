class Circuit:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Gets a list of nodes
    def getNodes(self):
        return list(self.gdict.keys())

    # You can get a specific node if u know the index of the node
    def getNodeByIndex(self,index):
        return self.getNodes()[index]

    def getEdges(self):
        edges = []
        for node in self.gdict:
            for edge in self.gdict[node]:
                if edge not in edges:
                    edges.append(edge)
        return edges

    

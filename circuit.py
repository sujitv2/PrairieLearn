class Node:
    def __init__(self, id, type, isGround, edges):
        self.id = id # int
        self.type = type # string
        self.isGround = isGround # bool
        self.edges = edges # map string direction to Edge obj

class Edge:
    def __init__(self, nodes):
        self.nodes = nodes # map string direction to Node obj



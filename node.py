class Node(object):
    def __init__(self):
        self.name = None
        self.children = {}
        self.column = None
        self.leaf = False
        self.classes = None
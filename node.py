class Node(object):
    def __init__(self):
        self.name = None
        self.children = {}
        self.column = None
        self.leaf = False
        self.classes = None
    def answer(self, level=0, ):
        result = ""

        if not self.leaf:
            for key, val in self.children.iteritems():
                result += "\t" * level
                result += self.name + ": " + key + "\n"
                result += val.answer(level + 1)
        else:
            result += "  " * level
            result += "answer: " + self.classes.keys()[0] + '\n'

        return result

    def __repr__(self):
        return self.answer()
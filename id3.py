import node as tnode
import numpy as np
from collections import Counter

class ID3(object):
    
    def __init__(self):
        self.result = None
        
    def gain(self, attr, subsets):
        n = attr.shape[0]
        subset_entropy = 0
        # Calculate the subset entropy
        for record in subsets:
            subset_entropy += (record.shape[0] / float(n)) * self.entropy(record)
        # Return the gain
        return self.entropy(attr) - subset_entropy
    
    def entropy(self, target_attr):
        n = target_attr.shape[0]
        data_entropy = 0
        # Calculate the entropy of the data for the target attribute
        for record in np.unique(target_attr):
            p = sum(target_attr == record) / float(n)
            data_entropy += p * np.log2(p)
        return -data_entropy
    
    def create_tree(self, params, ans, attributes=None):
        if attributes is None or len(attributes) != params.shape[1]:
            fattributes = np.arange(params.shape[1])
        else:
            fattributes = attributes

        self.result = self.setNodes(params, ans, fattributes)
        
    def setNodes(self, params, ans, attributes, level=0):
        node = tnode.Node()
        gain = 0
        columns = None
        names = None
        splits = None

        for i in xrange(params.shape[1]):
            values = np.unique(params[:, i])
            subsets = []
            conditions = []

            if len(values) < 1:
                continue
            # Create y subset for each of the column values
            for val in values:
                conditions.append(params[:,i] == val)
                subsets.append(ans[params[:,i] == val])

            # Calculate information gain of the column
            new_gain = self.gain(ans, subsets)

            if new_gain > gain:
                columns = i
                names = values
                gain = new_gain
                splits = conditions
        
        # check if node is a leaf, then set it
        if columns == None or len(np.unique(ans)) == 1:
            node.leaf = True
            node.classes = Counter(ans)
            node.name = node.classes.most_common(1)[0][0]
        #
        else:
            node.name = attributes[columns]
            node.column = columns
            # for each unique value we create a subset of the parameters and the answers
            for i, val in enumerate(names):
                # print val
                sub_p = np.delete(params, columns, axis=1)
                sub_p = sub_p[splits[i]]
                # print sub_p
                # print "\n"
                new_attributes = np.delete(attributes, columns)
                sub_a = ans[splits[i]]
                # print sub_a
                # print "\n"
                node.children[val] = self.setNodes(sub_p, sub_a, new_attributes, level + 1)
        return node
    
    def __str__(self):
        return str(self.result)
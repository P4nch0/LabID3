import node as tnode
import numpy as np
from collections import Counter
class ID3(object):
    def __init__(self):
        self.root = None
        self.feature_names = None
        self.categorical = None
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
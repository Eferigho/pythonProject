class Node:
    """
    An object for storing a single node models into two attributes
    """
    data = None
    next_node =None
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
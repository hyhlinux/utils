class LNode(object):
    """docstring for LNode"""
    
    def __init__(self, elem, next_=None):
        super(LNode, self).__init__()
        self.elem = elem
        self.next = next_

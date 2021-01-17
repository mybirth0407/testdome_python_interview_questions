import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    r2 = root
    while r2 != None:
        if r2.value == value:
            return True
        elif r2.value > value:
            r2 = r2.left
        else:
            r2 = r2.right
    return False
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))
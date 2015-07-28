# some data structure and useful function
class ListNode:
    def __init__(self,value):
        self.val = value
        self.next = None

def print_list(node):
    a = node
    res = []
    while a:
        res += [a.val]
        a = a.next
    print res


def create_list(nums):
    x = map(lambda x:ListNode(x),nums)
    head = x[0]
    for i in range(len(nums)-1):
        x[i].next = x[i+1]
    return head

# remove the list node after 'node'

def remove_node(node):
    if not node or not node.next:
        return
    a = node.next.next
    #node.next.next = None
    node.next = a



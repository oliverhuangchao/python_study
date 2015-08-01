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
    if not nums:
        return None
    x = map(lambda x:ListNode(x),nums)
    head = x[0]
    for i in range(len(nums)-1):
        x[i].next = x[i+1]
    return head

#insert newnode after the given node
def insert_node(node,newnode):
    newnode.next = node.next
    node.next = newnode


# remove the list node after 'node'
def remove_node(node):
    if not node or not node.next:
        return
    a = node.next.next
    #node.next.next = None
    node.next = a

# merge two sorted list in one list
# O(1) space and linear time
def merge_sorted_list(head1,head2):
    begin = basic.ListNode(-1)
    tmp = begin
    a = head1
    b = head2
    while a and b:
        if a.val <= b.val:
            tmp.next = a
            a = a.next
        else:
            tmp.next = b
            b = b.next
        tmp = tmp.next

    if a:
        tmp.next = a
    if b:
        tmp.next = b
    return begin.next


# mergesort for list
# time O(nlog(n))
# constant space
def mergeSort(head):
    slow = head
    fast = head
    if not fast or not fast.next:
        return head
    if not fast.next.next:
        first = fast
        second = fast.next# sequence is quite important
        first.next = None
        #second = fast.next# put it here is wrong
        return merge_sorted_list(first,second)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    tmp = slow.next
    slow.next = None
    first = mergeSort(head)
    second = mergeSort(tmp)
    return merge_sorted_list(first,second)


# return the size of the list
def get_length(a):
    count = 0
    while a:
        count += 1
        a = a.next
    return count


# partition a list with a target
def partition_list(head,target):
    begin = ListNode(-1)
    begin.next = head
    # put all the value small then target at the front
    if not head or not head.next:
        return begin.next
    a = begin
    while a.next:
        if a.next.val < target:
            tmp = a.next
            remove_node(a)
            insert_node(begin,tmp)
            if a == begin:
                a = a.next
        else:
            a = a.next
    #put all the value bigger than target at the last
    b = begin
    while b.next and b.next.val < target:
        b = b.next
    a = b
    while a.next:
        if a.next.val == target:
            tmp = a.next
            ll.remove_node(a)
            ll.insert_node(b,tmp)
            if a == b:
                a = a.next
        else:
            a = a.next
    return begin.next








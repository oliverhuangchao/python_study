import mylist as ll
import pdb


# check if a list is a palidrome
# O(n2) solution

def isPalidrome(head):
    if not head or not head.next:
        return True
    size = ll.get_length(head)
    return rec(head,size-1)


def rec(head,size):
    if size < 1:
        return True
    a = head
    i = 0
    for i in range(size):
        a = a.next
    return head.val == a.val and rec(head.next,size-2)
   

head1 = ll.create_list([1,2,2])
#head2 = ll.create_list([5,9,2])
ll.print_list(head1)
#ll.print_list(head2)
print isPalidrome(head1)
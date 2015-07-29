import mylist as ll

# find the kth element in the list


def return_kth(head,k):
    size = ll.get_length(head)
    if not head or k>size:
        print "invalid input"
        return 0
    #far = size-k+1
    start = head
    end = head
    for i in range(k):
        end = end.next
    while end:
        start = start.next
        end = end.next
    return start.val





head = ll.create_list([1,2,3,4,5])
ll.print_list(head)
print return_kth(head,2)


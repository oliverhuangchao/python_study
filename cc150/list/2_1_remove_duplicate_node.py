# remove duplicate from unsorted list
import basic

# use hash table to remove duplicate
# time O(n)
# space O(n)
def remove_duplicate(head):
    check = set()
    a = head
    check.add(a.val)
    while a.next:
        if a.next.val in check:
            basic.remove_node(a)
        else:
            check.add(a.next.val)
            a = a.next
        if not a.next:
            break

# if the temp buffer is not allowed
# I have to sort the list using merge sort and then linear scan
# O(nlog(n)) time       
# space O(1)
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


def remove_duplicate_with_sort(head):
    z = mergeSort(head)
    if not z or not z.next:
        return z
    first = z
    second = z.next
    while second:
        if first.val == second.val:
            basic.remove_node(first)
            second = first.next
        else:
            first = second
            second = first.next
    return z



nums = [1,1,3,5,1,1,1,2,1,2,1,1,3,4,5,1,1,6]
#nums = [1,4,5]
x = basic.create_list(nums)
basic.print_list(x)
#res = mergeSort(x)
#basic.print_list(res)

res = remove_duplicate_with_sort(x)
basic.print_list(res)


# basic.print_list(x)
# y = basic.create_list([2,4,6])
# basic.print_list(y)
# res = merge_sorted_list(x,y)
# basic.print_list(res)

# head = basic.create_list(nums)
# basic.print_list(head)
# remove_duplicate(head)
# basic.print_list(head)




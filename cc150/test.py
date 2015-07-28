# remove duplicate from unsorted list
import basic



# use hash table to remove duplicate
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
       




nums = [1,1,1,1,1,2,1,2,1,1,3,4,5,1,1,6]
#nums = [1,2,1,3,5,3,5,1,2,6,1]
#nums = [1,2,1,3,5,3,5,1,2,6,1]
head = basic.create_list(nums)
basic.print_list(head)
remove_duplicate(head)
basic.print_list(head)




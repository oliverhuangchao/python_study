import mylist as ll
import pdb
# add two number writtern in list

# start from the end to start
def add(head1,head2):
    flag = 0
    res = 0
    i = 0
    while head1 and head2:
        tmp = head1.val + head2.val + flag
        flag = tmp / 10
        res += (10**i)*(tmp%10)
        i += 1
        head1 = head1.next
        head2 = head2.next
    if head1:
        tmp = head1.val+flag
        flag = tmp / 10
        res += (10**i)*(tmp%10)
        i += 1
        head1 = head1.next
    if head2:
        tmp = head2.val+flag
        flag = tmp / 10
        res += (10**i)*(tmp%10)
        i += 1
        head2 = head2.next
    return res

# start from the begining
# ge
def add2(head1,head2):

    # get each lenght and makup 0 nodes for the shorter one
    l1 = ll.get_length(head1)
    l2 = ll.get_length(head2)
    #print "%d,%d" % (l1,l2)

    if l1>=l2:
        while l1 > l2:
            zero = ll.ListNode(0)
            zero.next = head2
            head2 = zero
            l2 += 1
    else: 
        while l1 < l2:
            zero = ll.ListNode(0)
            zero.next = head1
            head1 = zero
            l1 += 1
    #print "%d,%d" % (l1,l2)
    ll.print_list(head1)
    ll.print_list(head2)
    res,flag = rec(head1,head2,l1-1)
    if flag == 1:
        return res+10**l1
    else:
        return res

def rec(head1,head2,i):
    if i == 0:
        tmp = head1.val+head2.val
        return (tmp%10,tmp/10)
    res = 0
    tmp = head1.val + head2.val
    head1 = head1.next
    head2 = head2.next
    other,flag = rec(head1,head2,i-1)
    return ((tmp+flag)%10*(10**i)+other,tmp/10)


head1 = ll.create_list([1,2,1,7,1,6])
head2 = ll.create_list([5,9,2])
ll.print_list(head1)
ll.print_list(head2)
print add2(head1,head2)
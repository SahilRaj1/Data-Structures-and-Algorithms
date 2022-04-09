""" Partition """

from LinkedList import LinkedList

def partition(ll,x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None


ll = LinkedList()
ll.add(1)
ll.add(6)
ll.add(2)
ll.add(4)
ll.add(5)
ll.add(3)
print(ll)

partition(ll, 3)
print(ll)
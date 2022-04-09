""" Return nth from last """

from LinkedList import LinkedList

def func(ll, n):
    p1 = ll.head
    p2 = ll.head
    for i in range(n):
        if p2 is None:
            return None
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1.value

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)

print(ll)

print(func(ll,2))
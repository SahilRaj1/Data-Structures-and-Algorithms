""" Sum Linked List """

from LinkedList import LinkedList

def sumLL(llA,llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result%10))
        carry = result//10
    if carry != 0:
        ll.add(carry)

    return ll

llA = LinkedList()
llA.add(4)
llA.add(9)
llA.add(3)

llB = LinkedList()
llB.add(8)
llB.add(0)
llB.add(6)

ll = sumLL(llA, llB)

print(ll)
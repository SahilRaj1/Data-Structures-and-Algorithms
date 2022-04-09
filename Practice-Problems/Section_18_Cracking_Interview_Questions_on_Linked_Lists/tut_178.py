""" Remove Duplicates """

from LinkedList import LinkedList

def remove_duplicates(ll, ll1):
    if ll.head is None:
        print("The linked list is empty")
    else:
        visited = set()
        tempNode = ll.head
        while tempNode:
            visited.add(tempNode.value)
            tempNode = tempNode.next
        for i in visited:
            ll1.add(i)
        return ll1


def remove_duplicates1(ll):
    if ll.head is None:
        print("The linked list is empty")
    else:
        tempNode = ll.head
        while tempNode:
            nextNode = tempNode
            while nextNode.next:
                if tempNode.value == nextNode.next.value:
                    nextNode.next = nextNode.next.next
                else:
                    nextNode = nextNode.next
            tempNode = tempNode.next
    return ll

ll = LinkedList()
ll1 = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(1)
ll.add(6)
print(ll)

# remove_duplicates(ll, ll1)
# print(ll1)

remove_duplicates1(ll)
print(ll)
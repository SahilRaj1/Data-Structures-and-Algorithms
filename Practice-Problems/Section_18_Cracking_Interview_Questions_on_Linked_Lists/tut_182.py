""" Intersection """

from LinkedList import LinkedList

def intersection(ll1, ll2):
    node1 = ll1.head
    while node1:
        node2 = ll2.head
        while node2
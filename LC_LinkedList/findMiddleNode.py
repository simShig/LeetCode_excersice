'''
LL: Find Middle Node ( ** Interview Question)
Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can only use one loop.


'''



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


    def hopTwice(self, cur):  # node -> True(whenFinished) or False(yet finished)
        cur = cur.next  # cur.next
        if cur is None:
            return True, cur
        else:
            cur = cur.next  # cur.next.next

        if cur is None:
            return True, cur
        elif cur.next is None:
            return True, cur
        else:
            return False, cur

    def find_middle_node(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.head
        slowP = self.head
        fastP = self.head
        flag = False
        while not flag:
            flag, fastP = self.hopTwice(fastP)
            slowP = slowP.next
            # print(f'sP = {slowP.value}, fP = {fastP.value}')
        return slowP
    ######################################


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)

"""
    EXPECTED OUTPUT:
    ----------------
    3

"""
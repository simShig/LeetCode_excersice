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
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def DFS_pr_o(self):        #preOrder
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def DFS_po_o(self):     #postOrder
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def DFS_in_o(self):     #inOrder
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)          
        traverse(self.root)
        return results
        




my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print('InOrder:')
print(my_tree.DFS_in_o())



"""
    EXPECTED OUTPUT:
    ----------------
    [18, 21, 27, 47, 52, 76, 82]

 """

print('PostOrder:')

print(my_tree.DFS_po_o())



"""
    EXPECTED OUTPUT:
    ----------------
    [18, 27, 21, 52, 82, 76, 47]

 """
print('PreOrder:')
print(my_tree.DFS_pr_o())

"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 18, 27, 76, 52, 82]

 """


                



 
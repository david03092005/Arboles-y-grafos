"""
Implementación Árboles Estructuras Enlazadas

"""

class Tree:
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def getData(self):
        ans = self.data
        return ans

    def getLeft(self):
        ans = self.left
        return ans

    def getRight(self):
        ans = self.right
        return ans

    def getParent(self):
        ans = self.parent
        return ans

    def preorder(self):
        pre = []
        pre.append(self.data)
        if self.left != None: pre.extend(self.left.preorder())
        if self.right != None: pre.extend(self.right.preorder())
        return pre

    def posorder(self):
        pos = []
        if self.left != None: pos.extend(self.left.posorder())
        if self.right != None: pos.extend(self.right.posorder())
        pos.append(self.data)
        return pos

    def inorder(self):
        inord = []
        if self.left != None: inord.extend(self.left.inorder())
        inord.append(self.data)
        if self.right != None: inord.extend(self.right.inorder())
        return inord

    def sum(self):
        ans = self.data
        if self.left != None: ans += self.left.sum()
        if self.right != None: ans += self.right.sum()
        return ans

node2 = node3 = node4 = node5 = node6 = node7 = node8 = node9 = node10 = node11 = node12 = node13 = node14 = node15 = None

node1 = Tree(4)
node2 = Tree(5, parent = node1)
node3 = Tree(1, parent = node1)
node4 = Tree(6, parent = node2)
node5 = Tree(3, parent = node2)
node6 = Tree(12, parent = node3)
node7 = Tree(1, parent = node4)
node8 = Tree(11, parent = node4)
node9 = Tree(17, parent = node5)
node10 = Tree(18, parent = node5)
node11 = Tree(8, parent = node7)
node12 = Tree(9, parent = node8)
node13 = Tree(21, parent = node10)
node14 = Tree(7, parent = node12)
node15 = Tree(11, parent = node13)

node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.right = node6
node4.left, node4.right = node7, node8
node5.left, node5.right = node9, node10
node7.right = node11
node8.left = node12
node10.left = node13
node12.left = node14
node13.left = node15

tree1 = node1

"""
tree1 = Tree(4,
             Tree(5,
                  Tree(6,
                       Tree(1,
                            None,
                            Tree(8, None, None)),
                       Tree(11,
                            Tree(9,
                                 Tree(7, None, None),
                                 None),
                            None)),
                  Tree(3,
                       Tree(17, None, None),
                       Tree(18,
                            Tree(21,
                                 Tree(11, None, None),
                                 None),
                            None))),
             Tree(1,
                  None,
                  Tree(12, None, None)))
"""

print(tree1.preorder())
print(tree1.inorder())
print(tree1.posorder())
print(tree1.sum())

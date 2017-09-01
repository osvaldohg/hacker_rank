# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
# by oz 

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
res=""
def preOrder(root):
    #Write your code here
       
    if root is not None:
        print root.data,
        preOrder(root.left),
        preOrder(root.right),
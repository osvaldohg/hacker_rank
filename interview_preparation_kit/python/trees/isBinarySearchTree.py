# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
# by oz
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    val=verifyBST(root,None,None)
    if val:
        print "Yes"
    else:
        print "No"
        
    exit()
        
def verifyBST(root,l = None, r = None):
    if root == None:
        return True
    
    if (r != None and root.data > r.data) : 
        return False
    
    if (r != None and root.data > r.data) : 
        return False
    
    return verifyBST(root.left, l, root) and verifyBST(root.right, root, r)
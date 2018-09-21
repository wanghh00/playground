# Definition for a binary tree node.
from collections import deque

def lst2tree(lst):
    if not lst:
        return None

    ln = len(lst)

    root = TreeNode(lst[0])
    q = deque()
    q.append([0, root])

    while q:
        i, cur = q.popleft()
        leftnum = 2*i+1
        if leftnum < ln and lst[leftnum] != None:
            cur.left = TreeNode(lst[leftnum])
            q.append([leftnum, cur.left])
        
        rightnum = leftnum + 1
        if rightnum < ln and lst[rightnum] != None:
            cur.right = TreeNode(lst[rightnum])
            q.append([rightnum, cur.right])

    return root

ARR = []
def firstrootaccess(node):
    if not node:
        return
    ARR.append(node.val)
    if node.left:
        firstrootaccess(node.left)
    if node.right:
        firstrootaccess(node.right)
    return

def lastrootaccess(node):
    if not node:
        return
    if node.left:
        lastrootaccess(node.left)
    if node.right:
        lastrootaccess(node.right)
    ARR.append(node.val)
    return



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right

tree1 = [3,5,1,6,2,0,8,None,None,7,4]
root = lst2tree(tree1)

#firstrootaccess(root)
#print ARR

#ARR = []
#lastrootaccess(root)
#print ARR

print Solution().lowestCommonAncestor(root, 5, 1).val

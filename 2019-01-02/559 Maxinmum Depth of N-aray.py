"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        queue = []
        queue.append((root,1))
        while queue:
            node,depth = queue.pop(0)
            if hasattr(node,"children"):
                queue.extend([(cnode,depth+1) for cnode in node.children])
        return depth
        

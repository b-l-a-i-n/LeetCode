"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def preorder(root: 'Node') -> List[int]:
        stack = [root]
        out = []
        while stack and stack[-1]:
            if stack[-1].children[::-1]:
                out.append(stack[-1].val)
                children = stack[-1].children[::-1]
                stack.pop()
                stack += children
            else:
                out.append(stack[-1].val)
                stack.pop()
        return out
# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.

# Example 1:
# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.

# Example 2:
# Input: root = [1], start = 1
# Output: 0
# Explanation: At minute 0, the only node in the tree is infected so we return 0.

from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        stack = [(root, None)]

        while stack:
            node, parent = stack.pop()

            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)

            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))

        queue = [start]
        seen = {start}

        ans = -1
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                for v in graph[node]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
                print(seen, queue)
                ans += 1

        return ans

"""
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

Example 2:
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

Example 3:
Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
"""
from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)

        edges_req = 0

        # Add edges for type 3 and count the required edges for Alice and Bob
        for edge in edges:
            if edge[0] == 3:
                edges_req += alice.union(edge[1], edge[2]) | bob.union(edge[1], edge[2])

        # Add edges for type 1 and count the required edges for Alice
        for edge in edges:
            if edge[0] == 1:
                edges_req += alice.union(edge[1], edge[2])

        # Add edges for type 2 and count the required edges for Bob
        for edge in edges:
            if edge[0] == 2:
                edges_req += bob.union(edge[1], edge[2])

        # Check if Alice and Bob are connected
        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_req
        else:
            return -1


class UnionFind:
    def __init__(self, n):
        self.components = n
        self.parent = [i for i in range(n + 1)]
        self.component_size = [1] * (n + 1)

    def find_parent(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)

        if parent_x == parent_y:
            return 0

        if self.component_size[parent_x] > self.component_size[parent_y]:
            self.component_size[parent_x] += self.component_size[parent_y]
            self.parent[parent_y] = parent_x
        else:
            self.component_size[parent_y] += self.component_size[parent_x]
            self.parent[parent_x] = parent_y

        self.components -= 1
        return 1

    def is_connected(self):
        return self.components == 1

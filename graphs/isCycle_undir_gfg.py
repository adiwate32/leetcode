"""
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

Example 1:
Input:
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}}
Output: 1
Explanation:
1->2->3->4->1 is a cycle.

Example 2:
Input:
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
"""
from typing import List


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [False] * V
        for i in range(V):
            if not vis[i]:
                if self.dfs(adj, V, i):
                    return True
        return False

    def dfs(self, adj, vis, src):
        vis[src] = True
        q = []
        q.append((src, -1))

        while q:
            node, par = q.pop(0)

            for nei in adj[node]:
                if not vis[nei]:
                    vis[nei] = True
                    q.append((nei, node))

                elif par != nei:
                    return True
        return False


# {
# Driver Code Starts
if __name__ == "__main__":

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if ans:
            print("1")
        else:
            print("0")

# } Driver Code Ends

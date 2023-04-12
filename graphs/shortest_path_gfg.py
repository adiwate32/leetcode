"""
Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i, 0<=i

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

Example:
Input:
n = 6, m= 7
edge=[[0,1,2],[0,4,1],[4,5,4]
,[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
Output:
0 2 3 6 1 5
"""
from typing import List
from collections import defaultdict


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        def topoSort(V, adj):
            # Code here
            def dfs(vis, adj, src, topo):
                vis[src] = True
                for nei, wt in adj[src]:
                    if not vis[nei]:
                        dfs(vis, adj, nei, topo)

                topo.append(src)

            topo = []
            vis = [False] * V

            for i in range(V):
                if not vis[i]:
                    dfs(vis, adj, i, topo)

            return topo

        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append((e[1], e[2]))

        topo = topoSort(n, adj)
        dist = [float("inf")] * n

        dist[0] = 0
        while topo:
            node = topo.pop()
            if dist[node] != float("inf"):
                for nei, wt in adj[node]:
                    dist[nei] = min(dist[node] + wt, dist[nei])

        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        return dist


# {
# Driver Code Starts
# Initial Template for Python 3

from typing import List


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        edges = IntMatrix().Input(m, 3)

        obj = Solution()
        res = obj.shortestPath(n, m, edges)

        IntArray().Print(res)
# } Driver Code Ends

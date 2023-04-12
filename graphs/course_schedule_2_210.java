package graphs;

import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        Map<Integer, List<Integer>> graph = new HashMap<>();

        int[] pre_map = new int[numCourses];

        for(int[] cr : prerequisites)
        {   
            int pre = cr[1];
            int course = cr[0];

            if(!graph.containsKey(pre))
            {
                graph.put(pre, new ArrayList<>());
            }

            graph.get(pre).add(course);
            pre_map[course]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for(int i =0; i < numCourses; i++)
        {
            if(pre_map[i] == 0)
            {
                q.add(i);
            }
        }

        int[] topo = new int[numCourses];
        int ind = 0;
        while(!q.isEmpty())
        {
            int pre = q.peek();
            q.remove();
            topo[ind++] = pre;

            if(graph.containsKey(pre))
            {
                for(int cr: graph.get(pre))
                {
                    pre_map[cr]--;

                    if(pre_map[cr] == 0)
                    {
                        q.add(cr);
                    }
                }
            }
        }

        if(ind == numCourses)
        {
            return topo;
        }

    return new int[] {};    
        
    }
} 
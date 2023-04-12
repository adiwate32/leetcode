package graphs;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
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
                q.offer(i);
            }
        }

        while(!q.isEmpty())
        {
            int pre = q.poll();

            if(graph.containsKey(pre))
            {
                for(int cr: graph.get(pre))
                {
                    pre_map[cr]--;

                    if(pre_map[cr] == 0)
                    {
                        q.offer(cr);
                    }
                }
            }
            numCourses--;
        }

        
    return numCourses==0;    
        
    }
}
package dynamic_programming;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {

        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 1);

        int mod = (int) Math.pow(10, 9) + 7;

        for(int i=1; i <=high; i++)
        {
            int z = dp.getOrDefault(i-zero, 0);
            int o = dp.getOrDefault(i-one, 0);

            int ans = (z + o) % mod;

            dp.put(i, ans);
        }

        int res = 0;
        for(int i=low; i<=high; i++)
        {
            res = (res + dp.get(i)) % mod;
        }
        
        return res;

        
    }
}
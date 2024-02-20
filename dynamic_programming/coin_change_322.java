package dynamic_programming;

import java.util.Arrays;

class Solution {
    public int coinChange(int[] coins, int amount) {
       int n = coins.length;

       int [][] dp = new int[n+1][amount+1];
       for(int i=0; i<=n; i++) Arrays.fill(dp[i], -1);
       int ans = knapsack(n, amount, coins, n, dp);
       return ans == 100000000 ? -1  : ans; 
    }

    public int knapsack(int idx, int val, int[] coins, int n, int[][] dp)
    {
        if(val == 0)
        {
            return 0;
        }

        if(idx == 0)
        {
            return 100000000;
        }

        if(dp[idx][val] != -1) return dp[idx][val];

        int rej = knapsack(idx-1, val, coins, n, dp);
        int sel = 100000000;

        if(val >= coins[idx-1])
        {
            sel = 1 + knapsack(idx, val-coins[idx-1], coins, n, dp);
        }

        dp[idx][val] = Math.min(rej, sel);
        return dp[idx][val];
    }
}
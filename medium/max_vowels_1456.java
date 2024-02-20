package medium;

import java.util.ArrayList;


class Solution {
    public ArrayList<ArrayList<Integer>> generateMatrix(int A) {

        int l = 0;
        int r = A-1;
        int u = 0;
        int d = A-1;

        int [][] mat = new int[A][A];

        int cnt = 1;

        while(cnt < A*A)
        {
            for(int i=l; i<=r && cnt <= A*A; i++)
            {
                mat[u][i] = cnt;
                cnt +=1;
            }

            for(int i=u+1; i<=d && cnt <= A*A; i++)
            {
                mat[i][r] = cnt;
                cnt +=1;
            }

            if(u != d)
            {
                for(int i=r-1; i>=l && cnt <= A*A; i--)
                {
                    mat[d][i] = cnt;
                    cnt +=1;
                }
            }

            if(l != r)
            {
                for(int i=d-1; i>=u+1 && cnt <= A*A; i--)
                {
                    mat[i][l] = cnt;
                    cnt +=1;
                }

            }

            u+=1;
            l+=1;
            d-=1;
            r-=1;
        }

        ArrayList<ArrayList<Integer>> list = new ArrayList<>();

        // populate the ArrayList with the values from the 2D array
        for (int i = 0; i < A; i++) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 0; j < A; j++) {
                row.add(mat[i][j]);
            }
            list.add(row);
        }

        return list;

    
    }
}
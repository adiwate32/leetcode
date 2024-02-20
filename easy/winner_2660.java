package easy;

class Solution {
    public int isWinner(int[] p1, int[] p2) {
        Integer total1 = 0;
        Integer total2 = 0;

        for (int i=0; i < p1.length; i++) {

            if(i>=2 && (p1[i-1] == 10 || p1[i-2] == 10))
            {
                total1 += 2 * p1[i];
            }
            else
            {
                total1 += p1[i];
            }

            if(i>=2 && (p2[i-1] == 10 || p2[i-2] == 10))
            {
                total2 += 2 * p2[i];
            }
            else
            {
                total2 += p2[i];
            }
            
        }

        if(total1 > total2)
        {
            return 1;
        }
        else if(total2 > total1)
        {
            return 2;
        }
        else 
        {
            return 0;
        }
        
        
    }
}
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        min_val = min(A)
        n = len(A)

        if n == 1:
            return 0

        cnt = 0
        while max(A) > min_val:
            for i in range(n):
                if i == 0:
                    A[i] = min(A[i], A[i + 1])

                elif i == n - 1:
                    A[i] = min(A[i - 1], A[i])

                else:
                    A[i] = min(A[i - 1], A[i + 1], A[i])
                print(A)
            cnt += 1

        return cnt


sol = Solution()
A = [2, 1, 10, 15]
print(sol.solve(A))

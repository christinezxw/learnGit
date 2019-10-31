class Solution:
    def commonSub(self, X, Y):
        m = len(X)
        n = len(Y)
        # commonSub = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        commonSub = [["" for _ in range(n + 1)] for _ in range(m + 1)]
        res = ""
        # sub = ""

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    commonSub[i][j] = ""
                elif X[i - 1] == Y[j - 1]:
                    # commonSub[i][j] = commonSub[i - 1][j - 1] + 1
                    commonSub[i][j] = commonSub[i - 1][j - 1] + X[i-1]
                    res = max(res, commonSub[i][j], key = len)
                else:
                    commonSub[i][j] = ""
        return res
    # def suffixTree(self, X, Y):
        
a = Solution()
print(a.commonSub("abc", "cba"))
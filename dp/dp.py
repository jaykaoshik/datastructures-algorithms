def longest_common_subsequence(x,y):
    dp = [[0]*len(y)]*len(x)
    for i in range(len(x)):
        for j in range(len(y)):
            if(x[i] != y[j]):
                dp[i][j] = max(dp[i-1][j] , dp[i][j - 1])
            else:
                dp[i][j] = 1 + dp[i-1][j-1]
    return dp[len(x)-1][len(y)-1]
print(longest_common_subsequence("AGGTAB","GXTXAYB"))
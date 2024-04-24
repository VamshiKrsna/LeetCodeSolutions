def tribonacci(n:int)->int:
    if n < 2:
        return n
    dp = [0,1,1]
    for i in range(3,n+1):
        next_val = dp[0] + dp[1] + dp[2]
        dp[0], dp[1], dp[2] = dp[1], dp[2], next_val
    return dp[2]

print(tribonacci(4))
print(tribonacci(25))
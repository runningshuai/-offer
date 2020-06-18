"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

# 和斐波那契一样的规律
def jumpFloor(number):
    dp = [0, 1, 2]
    if number<=2:
        return dp[number]
    for i in range(3, number + 1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[-1]

print(jumpFloor(4))
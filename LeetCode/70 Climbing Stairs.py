# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 




# Base cases:
# if n <= 0, then the number of ways should be zero.
# if n == 1, then there is only way to climb the stair.
# if n == 2, then there are two ways to climb the stairs. One solution is one step by another; 
# the other one is two steps at one time.

# The key intuition to solve the problem is that given a number of stairs n, if we know the number ways to get to the points [n-1] 
# and [n-2] respectively, denoted as n1 and n2 , then the total ways to get to the point [n] is n1 + n2. Because from the [n-1] 
# point, we can take one single step to reach [n]. And from the [n-2] point, we could take two steps to get there. 
# There is NO overlapping between these two solution sets, because we differ in the final step.


class Solution(object):
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)    

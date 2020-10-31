class Solution:
    def climbStairs(self, n: int) -> int:
        
        # main idea:
        # This is a classic Dynamic Programming problem
        # f(n) = number of ways you can climb to the nth step
        # f(n) = f(n – 1) + f(n – 2),
        # Set base cases f(1) = 1, f(2) = 2 and you are almost done.
        # calculate f(n) easily by storing previous values in an one dimension array
        
        if n==1:
            return 1
        if n==2:
            return 2
        
        # n >= 3
        my_array = [0]*(n+1)
        my_array[1] = 1
        my_array[2] = 2
        print(my_array)

        # same recurrence formula defined by the Fibonacci sequence (with different base cases, though)
        for i in range(3, n+1):
            my_array[i] = my_array[i-2] + my_array[i-1]
        
        distinct_ways = my_array[n]
        return distinct_ways
        

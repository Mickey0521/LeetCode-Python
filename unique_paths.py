class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # cannot use 'martix = [[0] * n] * m' <--- (wrong)
        # What this code does is creating three references to the same row. 
        
        # Therefore you need to use list comprehension
        # have to use 'martix = [ [0]*n for _ in range(m)]'
        # or 'martix = [[0 for j in range(M)] for i in range(N)]''

        # see: https://stackoverflow.com/questions/18449136/initialize-empty-matrix-in-python
        
        # When you reach row = m and col = n, 
        # you know you’ve reached the bottom-right corner
        
        # Bottom-up dynamic programming
        # Using the base case, we can build our way up to our solution at grid (m-1, n-1)
        my_matrix = [ [0 for j in range(n)] for i in range(m) ]
        print(my_matrix)
        for i in range(m):
            my_matrix[i][0] = 1
        for j in range(n):
            my_matrix[0][j] = 1
        print(my_matrix)

        # dynamic programming
        for i in range(1,m):
            for j in range(1,n):
                my_matrix[i][j] = my_matrix[i-1][j] + my_matrix[i][j-1]
        
        num_paths = my_matrix[m-1][n-1]
        return num_paths
        

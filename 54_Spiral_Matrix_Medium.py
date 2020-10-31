class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if matrix == []:
            return []
        
        test_matrix = [ [ 1, 2 ], [ 4, 5 ], [ 7, 8 ] ]
        print( len(test_matrix) )
        print( len(test_matrix[0]) )
        
        top = 0
        bottom = len(matrix)-1
        left= 0
        right = len(matrix[0])-1
        
        new_list = []
        
        # we define the directions
        # 0: go right
        # 1: go down
        # 2: go left
        # 3: go up
        direction = 0 
                
        while True:
            # 0: go right
            if direction == 0:
                for i in range(left, right+1):
                    new_list.append(matrix[top][i])
                top += 1
            # 1: go down
            elif direction == 1:
                for i in range(top, bottom+1):
                    new_list.append(matrix[i][right])
                right -=1
            # 2: go left
            # note: be careful about the 'range'
            elif direction == 2:
                for i in range(right, left-1, -1):
                    new_list.append(matrix[bottom][i])
                bottom -=1
            # 3: go up
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    new_list.append(matrix[i][left])
                left +=1
            
            # change the direction!!!
            direction = (direction+1) % 4
            
            if top > bottom or left > right:
                return new_list

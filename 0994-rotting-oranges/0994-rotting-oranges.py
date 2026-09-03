from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        queue = deque()
        fresh = 0 

        def explore(row: int,col: int) -> int:

            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or grid[row][col] == 2:

                return 0

            grid[row][col] = 2
            queue.append((row,col))

            return 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                
                if grid[i][j] == 1:
                    fresh += 1


        while queue:

            current_level = len(queue)

            fresh_going_in = fresh
            for _ in range(current_level):
                r,c = queue.popleft()
                fresh -= explore(r+1,c) + explore(r-1,c) + explore(r,c+1) + explore(r,c-1)

            if fresh < fresh_going_in:
                minutes += 1
            
        
        if fresh > 0:

            return -1

        else:

            return minutes

                



        
        
# Recursive DFS. Every "1" not seen yet is a new island; explore sinks the
# whole island by flipping its cells to "0" so nothing is counted twice.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        islands = 0 

        def explore(row,col):

            if row < 0 or row >= rows or col < 0 or col >= cols:

                return
                
            elif grid[row][col] == "0":
                
                return

            else:

                grid[row][col] = "0"
                explore(row-1,col)
                explore(row+1,col)
                explore(row,col+1)
                explore(row,col-1)


        for row in range(rows):
            for col in range(cols):
                    if grid[row][col] == "1":
                        islands += 1
                        explore(row,col)
               

        return islands
            


            


        
        
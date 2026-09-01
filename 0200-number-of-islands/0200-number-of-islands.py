# Revision. Same flood fill, now iterative (recursive version kept in the
# -recursive file). Leaning on the Python call stack gives me the "ick" —
# an explicit stack does the same walk by hand, and no grid can blow the
# recursion limit.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        islands = 0 

        def explore(row,col):

            stack = [(row,col)]

            while stack:

                r,c = stack.pop()

                if r < 0 or r >= rows or c < 0 or c >= cols:

                    continue
                
                if grid[r][c] == "0":

                    continue


                grid[r][c] = "0"
                stack.append((r+1,c))
                stack.append((r-1,c))
                stack.append((r,c+1))
                stack.append((r,c-1))


        for row in range(rows):
            for col in range(cols):
                    if grid[row][col] == "1":
                        islands += 1
                        explore(row,col)
               

        return islands
            


            


        
        
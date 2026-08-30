class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        total_elements = 0
        result = []
        untangled = []

        for row in mat:
            total_elements += len(row)
            untangled += row


        if (r * c) != total_elements:
            return mat

        left,right = 0,0

        for i in range(r):
            
            left = i * c
            right = left + c
            new_row = untangled[left:right]

            result.append(new_row)

        return result




        





        

        
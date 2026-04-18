class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m= len(matrix)
        n= len(matrix[0])
        l=0
        k= m*n-1

        while l<=k:
            mid = l+ (k-l)//2
            i=mid//n
            j=mid%n
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                k=mid-1
            else:
                l=mid+1
        return False
            

        
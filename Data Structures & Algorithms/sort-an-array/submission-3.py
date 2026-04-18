class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n= len(nums)

        def quicksort(arr):
            if len(arr)<=1:
                return arr

            pivot = arr[len(arr)//2]
            left_arr = [ i for i in arr if i<pivot]
            right_arr=[i for i in arr if i>pivot]
            mid = [i for i in arr if i==pivot]

            return quicksort(left_arr)+mid+quicksort(right_arr)

        return quicksort(nums)

        
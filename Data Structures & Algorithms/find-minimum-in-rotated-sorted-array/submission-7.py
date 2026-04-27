class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        while l + 1 < r:
            middle = (l + r) // 2
            print(f"middle of {l} and {r} is {middle}")
            print(l, middle, r)
            print()
            
            if nums[middle] > nums[l] and nums[middle] < nums[r]:
                # go left
                print("need to go left", l, middle, r)
                print("need to go left", nums[l], nums[middle], nums[r])
                print()
                r = middle
                print("went left", l, middle, r)
                print("went left", nums[l], nums[middle], nums[r])
                print()
            if nums[middle] > nums[l] and nums[middle] > nums[r]:
                # go right
                print("need to go right", l, middle, r)
                print("need to go right", nums[l], nums[middle], nums[r])
                l = middle
                print("went right", l, middle, r)
                print("went right", nums[l], nums[middle], nums[r])
                print()
            if nums[middle] < nums[l] and nums[middle] < nums[r]:
                # go left
                print("need to go left", l, middle, r)
                print("need to go left", nums[l], nums[middle], nums[r])
                print()
                r = middle
                print("went left", l, middle, r)
                print("went left", nums[l], nums[middle], nums[r])
                print()
            
        return min(nums[l], nums[r])
            
            
            
            # if nums[middle] < nums[l] and nums[middle] > nums[r]:
            #     #go left
    


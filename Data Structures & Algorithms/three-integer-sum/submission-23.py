class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        visited_nums = set()

        for i in range(len(nums)):
            if nums[i] in visited_nums:
                continue
            if nums[i] > 0:
                break
            visited_nums.add(nums[i])
            target = -1 * nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue
    
                addition = nums[j] + nums[k]
                if addition > target:
                    k -= 1
                elif addition < target:
                    j += 1
                else:
                    # if [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])
                    if nums[k - 1] != nums[k]: 
                        k-=1 # or j += 1
                    elif nums[j + 1] != nums[j]: 
                        j+=1 # or j += 1
                    else:
                        while j < k and nums[k] + nums[j] + nums[i] == 0:
                            k-=1
                            # j+=1
                        
        return res


# complexity: O(n**2) O(n)
# [-2,0,1,1,2]




# for the result of three numbers to be 0, one of them must be negative, so the loop must stop when
# we reach a strictly positive number

# [-4, -1, 0, 1, 2]
        
# nums[i] + nums[j] + nums[k] = 0
# nums[i] + nums[j] = - nums[k]
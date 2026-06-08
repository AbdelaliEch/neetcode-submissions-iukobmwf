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
                addition = nums[j] + nums[k]
                if addition > target:
                    k -= 1
                elif addition < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
                    while j < k and nums[k] == nums[k + 1]:
                        k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j+=1
                        
        return res





# complexity: O(n**2) O(n)
# for the result of three numbers to be 0, one of them must be negative, so the loop must stop when
# we reach a strictly positive number

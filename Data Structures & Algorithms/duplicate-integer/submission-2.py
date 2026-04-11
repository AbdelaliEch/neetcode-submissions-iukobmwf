class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False

        # my_dict = dict()
        # for num in nums:
        #     if num in my_dict:
        #         return True
        #     else:
        #         my_dict.add(num)
        # return False

# Time complexity: O(n)
# Space complexity: O(n)

# Time: you visit each element once → O(n)
# Space: worst case you store all n elements → O(n)

# Using a dict or a set is the same in this case, same complexity, a set
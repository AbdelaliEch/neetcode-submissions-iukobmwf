class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums) # O(n)
        
        visited = set()

        count = 0
        max_count = 0
        
        for num in nums_set:
            if num not in visited:
                num2 = num
                while num2 in nums_set:
                    visited.add(num2)
                    num2 += 1
                    count += 1
                    print(count)
                if count > max_count:
                    max_count = count
                    count = 0
            count = 0
        return max_count
            




        # while minimum <= maximum:
        #     if minimum in nums_set:
        #         if minimum + 1 in nums_set:
        #             count += 1
        #             print(f"adding count when minimum is {minimum} because {minimum + 1} in set, count is {count}")
        #         else:
        #             print("minimum + 1 not in nums_set")
        #             if count > max_count:
        #                 max_count = count
        #             count = 1
        #     minimum += 1
        # return max_count

            
                
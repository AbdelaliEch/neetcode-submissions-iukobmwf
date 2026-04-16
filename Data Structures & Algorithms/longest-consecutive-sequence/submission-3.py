class Solution:
    # def calculate_difference(self, my_dict):
         

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums) # O(n)
        minimum = min(nums_set)
        maximum = max(nums_set)

        count = 1
        max_count = 1
        while minimum <= maximum:
            if minimum in nums_set:
                if minimum + 1 in nums_set:
                    count += 1
                    print(f"adding count when minimum is {minimum} because {minimum + 1} in set, count is {count}")
                # print(count, max_count)
                else:
                    print("minimum + 1 not in nums_set")
                    if count > max_count:
                        max_count = count
                    count = 1
            minimum += 1
        return max_count

            
                
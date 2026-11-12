class Solution:
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        output = []

        def dfs(i, current_partition):
            if i == len(s):
                output.append(current_partition.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    current_partition.append(s[i:j+1])
                    dfs(j + 1, current_partition)
                    current_partition.pop()

        dfs(0, [])
        return output
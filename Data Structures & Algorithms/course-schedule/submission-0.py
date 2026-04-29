class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            adj_list[crs].append(preq)
        print(adj_list)

        dfs_done_on = set()
        current_path = set()

        def dfs(crs):
            if crs in current_path:
                return False
            if crs in dfs_done_on:
                return True

            current_path.add(crs)
            for preq in adj_list[crs]:
                if dfs(preq) == False:
                    return False
            current_path.remove(crs)
            dfs_done_on.add(crs)
            return True

        for crs in adj_list:
            if dfs(crs) == False:
                return False
        return True


# adj_list = {0: [], 1: [0], 2: []}
# current_path = {0}
# dfs_done_on = {}
# output = []


# prerequisites = {0: [1]}
# prerequisites = {0: [1]}
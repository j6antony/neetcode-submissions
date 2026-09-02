class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #study this style it is cleaner to write
        prereq = {i:[] for i in range(numCourses)}

        #populate the prereq hashmap
        for i in prerequisites:
            prereq[i[0]].append(i[1])
        #dfs visited set to track what has been visited:
        visited = set()
        def dfs(i):
            if not prereq[i]:
                return True
            if i in visited:
                return False
            else:
                visited.add(i)
                for pre in prereq[i]:
                    if not dfs(pre):
                        return False;
                visited.remove(i)
                prereq[i] = [];
                return True
        for i in prereq:
            if not dfs(i):
                return False
        return True
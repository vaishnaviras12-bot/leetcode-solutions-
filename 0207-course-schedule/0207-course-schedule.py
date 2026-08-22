class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visited = set()
        path = set()

        def dfs(node):
            visited.add(node)
            path.add(node)

            for neighbour in graph[node]:

                if neighbour not in visited:
                    if dfs(neighbour):
                        return True

                elif neighbour in path:
                    return True

            path.remove(node)
            return False

        for course in range(numCourses):
            if course not in visited:
                if dfs(course):
                    return False

        return True
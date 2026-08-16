from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        actual_color = image[sr][sc]

        if actual_color == color:
            return image

        queue = deque()
        queue.append((sr,sc))

        image [sr][sc] =color 

        rows = len(image)
        coloum = len(image[0])

        directions = [
            (-1,0),(1,0),(0,-1),(0,1)
        ]
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr = dr+r
                nc = dc+c
                if 0<=nr<rows and 0<=nc<coloum:
                    if image[nr][nc] == actual_color:
                        image[nr][nc] = color
                        queue.append((nr,nc))
        return image

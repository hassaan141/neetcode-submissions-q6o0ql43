class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        visited_atl = set()
        visited_pcf = set()

        for c in range(COLS):
            self.explore(heights, 0, c, visited_pcf, heights[0][c])
            self.explore(heights, ROWS - 1, c, visited_atl, heights[ROWS-1][c])

        for r in range(ROWS):
            self.explore(heights, r, 0, visited_pcf, heights[r][0])
            self.explore(heights, r, COLS - 1, visited_atl, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_atl and (r, c) in visited_pcf:
                    res.append((r, c))
        
        return res


    def explore(self, heights, r, c, visited, prevHeight):

        rowBound = 0 <= r < len(heights)
        colBound = 0 <= c < len(heights[0])
        if not rowBound or not colBound:
            return
        
        if (r, c) in visited:
            return

        if prevHeight > heights[r][c]:
            return

        visited.add((r, c))
        self.explore(heights, r - 1, c, visited, heights[r][c])
        self.explore(heights, r + 1, c, visited, heights[r][c])
        self.explore(heights, r, c - 1, visited, heights[r][c])
        self.explore(heights, r, c + 1, visited, heights[r][c])


    
        
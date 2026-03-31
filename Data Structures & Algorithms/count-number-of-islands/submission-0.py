class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(0, len(grid), 1):
            for c in range(len(grid[0])):
                count += self.explore(grid, r, c, visited)

        return count

    def explore(self, grid, r, c, visited):
        rowInbounds = 0 <= r and r < len(grid)
        colInbounds = 0 <= c and c < len(grid[0])
        if not rowInbounds or not colInbounds:
            return 0
        
        if (r, c) in visited:
            return 0
            
        if grid[r][c] == '0':
            return 0

        count = 0
        visited.add((r, c))

        self.explore(grid, r - 1, c, visited)
        self.explore(grid, r + 1, c, visited)
        self.explore(grid, r, c - 1, visited)
        self.explore(grid, r, c + 1, visited)

        return 1
    






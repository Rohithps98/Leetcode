from heapq import heappop, heappush
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If start or end is blocked, return -1
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        # Priority queue (min-heap) -> (cost, steps, row, col)
        heap = [(1 + self.heuristic(0, 0, n), 1, 0, 0)]
        
        # 8-directional movement
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Visited set
        visited = set()

        while heap:
            _, steps, r, c = heappop(heap)  # Get the best candidate
            
            # If reached the destination
            if (r, c) == (n - 1, n - 1):
                return steps
            
            if (r, c) in visited:
                continue  # Skip already processed nodes
            
            visited.add((r, c))  # Mark as visited
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    heappush(heap, (steps + 1 + self.heuristic(nr, nc, n), steps + 1, nr, nc))

        return -1  # No valid path found

    # Heuristic: Diagonal Distance
    def heuristic(self, x: int, y: int, n: int) -> int:
        return max(abs(x - (n - 1)), abs(y - (n - 1)))

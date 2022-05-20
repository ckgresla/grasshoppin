# Question Link- https://leetcode.com/problems/number-of-islands/




# Breadth First Search Approach
class Solution:
	def bfs(self, grid, r, c, m, n, d):
		q = list()
		q.append((r, c))		
		while q:
			i, j = q.pop()
			grid[i][j] = "-1" #indicies we traverse get marked as neg
			for r, c in d:
				new_r = r + i
				new_c = c + j 
				if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and grid[new_r][new_c] == "1":
					q.append((new_r, new_c))

	def numIslands(self, grid):
		d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		m, n = len(grid), len(grid[0]) #dims of grid to search
		count = 0 #init count of islands, item to return 

		for i in range(m):
			for j in range(n):
				if grid[i][j] == "1":
					self.bfs(grid, i, j, m, n, d)
					count+=1
		return count



# Question Link- https://leetcode.com/problems/flood-fill/




# A Solution Using Breadth-First Search 
class Solution:
	def floodFill(self, image, sr, sc, newColor):
		row_length = len(image) 
		col_length = len(image[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] #4 directions from current "pixel"
		current = image[sr][sc] #current location given by func input (sr = row_index, sc = col_index)
		
		q = [[sr, sc]]
		while q:
			r, c = q.pop(0) #returns the values in list item 1
			image[r][c] = newColor #update w newColor
			for r_, c_ in directions:
				if 0<=r+r_<row_length and 0<=c+c_<col_length and image[r+r_][c+c_]==current and image[r+r_][c+c_]!=newColor:
					q.append([r+r_, c+c_])
	
		return image



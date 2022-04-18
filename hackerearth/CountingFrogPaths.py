# Question Link- https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/


x, y, s, t = (int(i) for i in input().split(" "))


j, c = t, 0

for i in range(0, t):
	if (j >= y and j <= + s):
		c += min(max(0, i-x+1), s+1)
	j -= 1

print(c)


"Exhausted today, partial solution from this guy- https://github.com/codereport/HackerEarth/blob/master/HourStorm_02_P1.py )

import sys

def traversal(p, q, a):
	r = 0
	s = 0
	while (r < p and s < q):
		for i in range(s, q):
			print(a[r][i], end=" ")
		r += 1
		for i in range(r, p):
			print(a[i][q - 1], end=" ")
		q -= 1
		if (r < p):
			for i in range(q - 1, (s - 1), -1):
				print(a[p - 1][i], end=" ")
			p -= 1
		if (s < q):
			for i in range(p - 1, r - 1, -1):
				print(a[i][s], end=" ")
			s += 1
			
rows = int(sys.argv[1])
cols = int(sys.argv[2])

a = []
for i in range(rows):
    T = []
    for j in range(cols):
        T.append(i*cols + j+1)
    a.append(T)
print(a)
        
# Call the function
traversal(rows, cols, a)




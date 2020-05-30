def get (s, t, i, j, D):
	if (D[i][j] != 2e9):
		return D[i][j]
	elif (i == 0 and j == 0):
		D[i][j] = 0
	elif (i == 0):
		D[i][j] = j
	elif (j == 0):
		D[i][j] = i
	else:
		if (s[i - 1] == t[j - 1]):
			x = 0
		else: 
			x = 1
		D[i][j] = min (get (s, t, i, j - 1, D) + 1, get (s, t, i - 1, j, D) + 1, get (s, t, i - 1, j - 1, D) + x)
	return D[i][j]



def lev (a, b):
	n = len (a)
	m = len (b)
	D = [[2e9] * (m + 1) for i in range (n + 1)]
	return get (a, b, n, m, D)

def StrDist (a, b):
	return lev (a, b) / (len (a) + len (b))


print (StrDist ("ABC12XYZ", "aBC12XY"))
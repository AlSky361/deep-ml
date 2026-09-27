def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	res = []

	if len(a[0]) != len(b):
		return -1

	for i in range(len(a)):
		sum = 0.0
		for j in range(len(a[i])):
			sum += a[i][j] * b[j]
		res.append(sum)

	return res
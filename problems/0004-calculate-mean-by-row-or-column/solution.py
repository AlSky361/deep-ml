def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	res = []
	m, n = len(matrix), len(matrix[0])

	if mode == "row":
		for i in range(m):
			avg = sum(matrix[i][j] for j in range(n)) / n
			res.append(avg)
	else:
		for j in range(n):
			avg = sum(matrix[i][j] for i in range(m)) / m
			res.append(avg)

	return res
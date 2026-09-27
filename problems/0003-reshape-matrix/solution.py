import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	m, n = len(a), len(a[0])
	m_new, n_new = new_shape

	if m * n != m_new * n_new:
		return []

	buffer = [a[i][j] for i in range(m) for j in range(n)]
	result = [[buffer[i * n_new + j] for j in range(n_new)] for i in range(m_new)]

	return result
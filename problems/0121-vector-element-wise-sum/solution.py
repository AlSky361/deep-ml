def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	flag = (n := len(a)) == len(b)
	if not flag:
		return -1
	return [a[i] + b[i] for i in range(n)]
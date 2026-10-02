import numpy as np

def cosine_similarity(A: np.ndarray, B: np.ndarray) -> float:
	if not (np.any(A) and np.any(A)):
		raise ValueError

	dot_prod = A @ B
	norm_A, norm_B = np.linalg.norm(A, ord=2), np.linalg.norm(B, ord=2)

	return dot_prod / (norm_A * norm_B)
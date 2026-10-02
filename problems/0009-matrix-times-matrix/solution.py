import numpy as np

def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    m1, m2 = np.array(a), np.array(b)
    return (m1 @ m2).tolist() if m1.shape[1] == m2.shape[0] else -1
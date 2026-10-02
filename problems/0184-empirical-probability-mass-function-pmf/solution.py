import numpy as np

def empirical_pmf(samples: list[int]) -> list[tuple[int, float]]:
    vals, counts = np.unique(samples, return_counts=True)
    
    probabilities = counts / len(samples)
    
    return list(zip(vals, probabilities))

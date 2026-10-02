import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    match (norm_type, arr.ndim):
        case ("l1", _):
            ord_ = 1
            arr = arr.ravel()
        case ("l2", _):
            ord_ = 2
            arr = arr.ravel()
        case ("linf", _):
            ord_ = np.inf
            arr = arr.ravel()
        case ("frobenius", 2):
            ord_ = "fro"
        case _:
            raise ValueError
    
    return float(np.linalg.norm(arr, ord=ord_))

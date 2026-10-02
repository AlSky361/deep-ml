import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    result = dict()
    grad = np.array(gradient)
    
    m = float(np.linalg.norm(grad))
    if m == 0:
        zero_direction = tuple(np.zeros_like(grad).tolist())
        return {
            'magnitude': 0.0,
            'direction': zero_direction,
            'descent_direction': zero_direction
        }
        
    d = tuple((grad / m).tolist())
    desc_d = tuple((-grad / m).tolist())
    
    result['magnitude'] = m
    result['direction'] = d
    result['descent_direction'] = desc_d
    
    return result

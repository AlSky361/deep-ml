import numpy as np

def quotient_rule_derivative(g: list, h: list, x: float) -> float:
    poly_g = np.poly1d(g)
    poly_h = np.poly1d(h)
    
    deriv_g = poly_g.deriv()
    deriv_h = poly_h.deriv()
    
    numerator = deriv_g(x) * poly_h(x) - poly_g(x) * deriv_h(x)
    denominator = poly_h(x) ** 2
    
    return numerator / denominator

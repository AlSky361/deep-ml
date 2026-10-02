import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    result = dict()

    vals, counts = np.unique(data, return_counts=True)
    variance = np.var(data)

    quantiles = np.quantile(data, [0.25, 0.5, 0.75]).astype(float)

    result['mean'] = np.mean(data)
    result['median'] = np.median(data)
    result['mode'] = vals[np.argmax(counts)]
    result['variance'] = variance
    result['standard_deviation'] = np.sqrt(variance)
    result['25th_percentile'] = quantiles[0]
    result['50th_percentile'] = quantiles[1]
    result['75th_percentile'] = quantiles[2]
    result['interquartile_range'] = quantiles[2] - quantiles[0]

    return result
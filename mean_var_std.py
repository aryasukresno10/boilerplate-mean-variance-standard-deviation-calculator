import numpy as np

def calculate(list):
    """
    Output:
    {
        'mean': [axis1, axis2, flattened],
        'variance': [axis1, axis2, flattened],
        'standard deviation': [axis1, axis2, flattened],
        'max': [axis1, axis2, flattened],
        'min': [axis1, axis2, flattened],
        'sum': [axis1, axis2, flattened]
    }
    """
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    data = np.array(list).reshape(3, 3)
    # data.mean(axis=1).tolist(), data.mean(axis=2).tolist(), data.mean().tolist()
    calculations = {
        'mean': [data.mean(axis=0).tolist(), data.mean(axis=1).tolist(), data.mean().tolist()],
        'variance': [data.var(axis=0).tolist(), data.var(axis=1).tolist(), data.var().tolist()],
        'standard deviation': [data.std(axis=0).tolist(), data.std(axis=1).tolist(), data.std().tolist()],
        'max': [data.max(axis=0).tolist(), data.max(axis=1).tolist(), data.max().tolist()],
        'min': [data.min(axis=0).tolist(), data.min(axis=1).tolist(), data.min().tolist()],
        'sum': [data.sum(axis=0).tolist(), data.sum(axis=1).tolist(), data.sum().tolist()]
    }


    return calculations

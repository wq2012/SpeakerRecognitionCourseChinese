def ComputeCosine(vec1, vec2):
    """Compute the cosine similarity between two vectors.
    
    Args:
        vec1: a list of floating point numbers
        vec2: a list of floating point numbers with the same length as vec1
        
    Returns:
        a floating point number for the cosine similarity
    """
    assert isinstance(vec1, list)
    assert isinstance(vec2, list)
    assert len(vec1) > 1
    assert len(vec1) == len(vec2)
    
    sum1 = 0.0
    sum2 = 0.0
    inner_prod = 0.0
    for x, y in zip(vec1, vec2):
        inner_prod += x * y
        sum1 += x * x
        sum2 += y * y
    return inner_prod / (sum1 * sum2) ** 0.5
    
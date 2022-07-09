import math

def ComputeSoftmax(vec):
    """Compute the softmax of a vector.

    Args:
        vec: a list of floating point numbers

    Returns:
        a list of floating point numbers with the same legnth as vec
    """
    assert isinstance(vec, list)
    assert len(vec) > 1

    # Add your code here
    max_num = max(vec)
    exp_vec = [math.exp(x - max_num) for x in vec]
    exp_sum = sum(exp_vec)
    result = [x / exp_sum for x in exp_vec]
    print(result)
    return result
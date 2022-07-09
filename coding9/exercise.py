import math

def ComputeCrossEntropy(p, q):
    """Compute the cross entropy between two distributions..

    Args:
        p: the reference, a list of floating point numbers, which is a
            one-hot vector
        q: the hypothesis, a list of floating point numbers, which are all
            non-negative and sum to 1

    Returns:
        a floating point number for the cross entropy
    """
    assert isinstance(p, list)
    assert isinstance(q, list)
    # p is a one-hot vector
    assert len(p) > 1
    assert sum(p) == 1
    assert min(p) == 0
    assert max(p) == 1
    # q is a probability
    assert sum(q) == 1
    assert len(q) == len(p)
    assert min(q) >= 0

    # Add your code here
    result = 0
    for x, y in zip(p, q):
        if x != 0:
            result -= x * math.log(y+0.001)
    print(result)
    return result
def ComputeZeroCross(signal):
    """Compute the zero cross rate of the signal.

    Args:
        signal: a list of floating point numbers

    Returns:
        an integer for the number of zero cross in the signal
    """
    assert isinstance(signal, list)
    assert len(signal) > 1

    # Add your code here
    Z = 0
    for i in range(1, len(signal)):
        Z += abs(sgn(signal[i]) - sgn(signal[i-1])) / 2
    return Z


def sgn(x):
    if x > 0:
      return 1
    elif x < 0:
      return -1
    else:
      return 0

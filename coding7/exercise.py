def ComputeConvolution(seq, kernel):
    """Compute 1-dim convolution.

    Args:
        seq: a list of floating point numbers as inputs
        kernel: a list of floating point numbers as the convolution kernel

    Returns:
        the output sequence, which is a list of floating point numbers
    """
    assert isinstance(seq, list)
    assert isinstance(kernel, list)
    assert len(seq) > 2
    assert len(kernel) >= 2
    assert len(seq) >= len(kernel)

    # Add your code here
    results = []
    for start in range(len(seq)):
        if start + len(kernel) > len(seq):
            break
        result = 0
        for i in range(len(kernel)):
           result += seq[start + i] * kernel[i]
        results.append(result)
    return results
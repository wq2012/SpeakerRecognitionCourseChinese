import cmath

def ComputeDFT(seq):
    """Compute Discrete Fourier Transform of a sequence.

    Args:
        seq: a list of floating point numbers

    Returns:
        a list of complex numbers
    """
    assert isinstance(seq, list)
    assert len(seq) > 2

    # Add your code here
    j = complex(0, 1)
    N = len(seq)
    results = []
    for k in range(N):
        result = 0
        for n in range(N):
            result += cmath.exp(-j*2*cmath.pi*n*k/N) * seq[n]
        results.append(result)
    print(results)
    return results
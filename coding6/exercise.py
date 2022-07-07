import math

def ComputeTNormScore(test_vec, enroll_vec, cohort_vecs):
    """Compute the t-norm cosine score.

    Args:
        test_vec: embedding of the runtime audio, which is a list of
            floating point numbers
        enroll_vec: embedding of the enrolled speaker, which is a list of
            floating point numbers
        cohort_vec: a list of cohort embeddings, where each embedding is a list
            of floating point numbers

    Returns:
        a floating point number for the normalized score
    """
    assert isinstance(test_vec, list)
    assert isinstance(enroll_vec, list)
    assert isinstance(cohort_vecs, list)
    assert len(test_vec) > 1
    assert len(test_vec) == len(enroll_vec)
    assert len(cohort_vecs) > 1
    for cohort_vec in cohort_vecs:
        assert len(test_vec) == len(cohort_vec)

    # Add your code here
    test_score = ComputeCosine(test_vec, enroll_vec)
    print('test_score:', test_score)
    cohort_scores = []
    for cohort_vec in cohort_vecs:
        cohort_scores.append(ComputeCosine(test_vec, cohort_vec))
    mean = sum(cohort_scores) / len(cohort_scores)
    std = math.sqrt(
        sum([(x - mean)**2 for x in cohort_scores]) / len(cohort_scores))
    print('mean:', mean, 'std:', std)
    normalized_score = (test_score - mean) / std
    print('normalized_score:', normalized_score)
    return normalized_score


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
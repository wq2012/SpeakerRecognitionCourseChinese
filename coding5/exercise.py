import csv

SCORES = 'scores.csv'

def ComputeEER():
    """Compute the Equal Error Rate from the data in scores.csv
    
    Returns:
        a floating point number for the equal error rate (between 0 and 1)
    """
    labels = []
    scores = []
    with open(SCORES) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            labels.append(int(row[0]))
            scores.append(float(row[1]))

    eer_threshold = None
    eer = None
    min_delta = 1
    threshold = 0.0
    while threshold < 1.0:
        accept = [score >= threshold for score in scores]
        fa = [a and (1-l) for a, l in zip(accept, labels)]
        fr = [(1-a) and l for a, l in zip(accept, labels)]
        far = sum(fa) / (len(labels) - sum(labels))
        frr = sum(fr) / sum(labels)
        delta = abs(far - frr)
        if delta < min_delta:
            min_delta = delta
            eer = (far + frr) / 2
            eer_threshold = threshold
        threshold += 0.005

    print('eer_threshold=', eer_threshold, 'eer=', eer)
    return eer

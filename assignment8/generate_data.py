import numpy as np
import pickle
import random

n_train = 10000
n_test = 100

train_samples = []
train_labels = []
test_samples = []
test_labels = []

for i in range(n_train + n_test):
  if i < n_train:
    samples = train_samples
    labels = train_labels
  else:
    samples = test_samples
    labels = test_labels

  label = random.choice([0, 1])
  start = random.uniform(-40.0, 40.0)
  sample = [start]
  next = start + random.uniform(-1, 5.0) * (-label * 2 + 1)
  sample.append(next)
  next = next + random.uniform(-2, 10.0) * (-label * 2 + 1)
  sample.append(next)
  next = next + random.uniform(-2, 10.0) * (-label * 2 + 1)
  sample.append(next)


  print("label:", label)
  print("sample:", sample)
  labels.append(label)
  samples.append(sample)

  data = {
    "train_samples": train_samples,
    "train_labels": train_labels,
    "test_samples": test_samples,
    "test_labels": test_labels,
  }

with open('data.pickle', 'wb') as f:
  pickle.dump(data, f)

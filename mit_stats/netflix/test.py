import numpy as np
import em
import common
from common import GaussianMixture, init
from naive_em import run

X = np.loadtxt("test_incomplete.txt")
X_gold = np.loadtxt("test_complete.txt")

K = 4
n, d = X.shape
seed = 0

# TODO: Your code here
# Initialize the mixture model with K=3 and seed=0
X = np.loadtxt("toy_data.txt")
K = 3
seed = 0
mixture, post = init(X, K, seed)

# Run the EM algorithm
mixture, post, log_likelihood = run(X, mixture, post)

print(f"Final log-likelihood: {log_likelihood}")
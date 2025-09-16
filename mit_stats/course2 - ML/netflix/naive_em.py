"""Mixture model using EM"""
from typing import Tuple
import numpy as np
from common import GaussianMixture



def estep(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step: Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the assignment
    """
    n, d = X.shape
    K = mixture.mu.shape[0]
    post = np.zeros((n, K))
    log_likelihood = 0.0

    for i in range(n):
        likelihoods = np.zeros(K)
        for j in range(K):
            # Compute the Gaussian likelihood for each component
            diff = X[i] - mixture.mu[j]
            likelihoods[j] = mixture.p[j] * (
                1 / ((2 * np.pi * mixture.var[j]) ** (d / 2))
            ) * np.exp(-0.5 * np.dot(diff, diff) / mixture.var[j])
        
        # Normalize to compute posterior probabilities
        total_likelihood = np.sum(likelihoods)
        post[i] = likelihoods / total_likelihood
        log_likelihood += np.log(total_likelihood)

    return post, log_likelihood


def mstep(X: np.ndarray, post: np.ndarray) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    n, d = X.shape
    K = post.shape[1]

    n_k = np.sum(post, axis=0)  # Effective number of points assigned to each cluster
    p = n_k / n  # Mixing proportions
    mu = np.dot(post.T, X) / n_k[:, None]  # Weighted means
    var = np.zeros(K)

    for j in range(K):
        diff = X - mu[j]
        var[j] = np.sum(post[:, j] * np.sum(diff ** 2, axis=1)) / (n_k[j] * d)

    return GaussianMixture(mu, var, p)


def run(X: np.ndarray, mixture: GaussianMixture,
        post: np.ndarray) -> Tuple[GaussianMixture, np.ndarray, float]:
    """Runs the mixture model

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the current assignment
    """
    prev_log_likelihood = None
    log_likelihood = None

    while prev_log_likelihood is None or log_likelihood - prev_log_likelihood > 1e-6 * abs(log_likelihood):
        prev_log_likelihood = log_likelihood

        # E-step
        post, log_likelihood = estep(X, mixture)
        #print(f"Log-likelihood: {log_likelihood}")

        # M-step
        mixture = mstep(X, post)

    return mixture, post, log_likelihood

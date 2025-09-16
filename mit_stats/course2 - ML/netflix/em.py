"""Mixture model for matrix completion"""
from typing import Tuple
import numpy as np
from scipy.special import logsumexp
from common import GaussianMixture


def estep(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step: Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the assignment

    """
    n, d = X.shape
    K = mixture.mu.shape[0]
    log_post = np.zeros((n, K))  # Log of posterior probabilities
    log_likelihood = 0.0

    for i in range(n):
        mask = X[i] > 0  # Identify observed entries
        for j in range(K):
            # Compute log of Gaussian likelihood for observed entries
            diff = X[i, mask] - mixture.mu[j, mask]
            log_gaussian = -0.5 * np.sum(diff**2 / mixture.var[j]) - \
                           0.5 * np.sum(mask) * np.log(2 * np.pi * mixture.var[j])
            
            # Add log of mixing proportion
            log_post[i, j] = log_gaussian + np.log(mixture.p[j] + 1e-16)

        # Normalize in the log domain using logsumexp
        log_sum = logsumexp(log_post[i])
        log_post[i] -= log_sum
        log_likelihood += log_sum

    # Convert log posterior probabilities back to normal probabilities
    post = np.exp(log_post)
    return post, log_likelihood



def mstep(X: np.ndarray, post: np.ndarray, mixture: GaussianMixture,
          min_variance: float = .25) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        post: (n, K) array holding the soft counts
            for all components for all examples
        mixture: the current gaussian mixture
        min_variance: the minimum variance for each gaussian

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    n, d = X.shape
    K = post.shape[1]

    # Initialize updated parameters
    new_mu = np.zeros((K, d))
    new_var = np.zeros(K)
    new_p = np.zeros(K)

    # Compute the effective number of points assigned to each cluster
    n_k = np.sum(post, axis=0)

    for j in range(K):
        # Mask for observed entries
        mask = X > 0

        # Update means (mu)
        weighted_sum = np.sum(post[:, j].reshape(-1, 1) * X * mask, axis=0)
        new_mu[j] = weighted_sum / (np.sum(post[:, j].reshape(-1, 1) * mask, axis=0) + 1e-16)

        # Update variances (var)
        diff = (X - new_mu[j]) * mask
        weighted_diff_squared = np.sum(post[:, j].reshape(-1, 1) * diff**2, axis=0)
        new_var[j] = np.sum(weighted_diff_squared) / (np.sum(post[:, j] * np.sum(mask, axis=1)) + 1e-16)
        new_var[j] = max(new_var[j], min_variance)  # Ensure variance is above the minimum

    # Update mixing proportions (p)
    new_p = n_k / n

    return GaussianMixture(new_mu, new_var, new_p)


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

        # E-step: Compute posterior probabilities and log-likelihood
        post, log_likelihood = estep(X, mixture)

        # M-step: Update the mixture model parameters
        mixture = mstep(X, post, mixture)

    return mixture, post, log_likelihood


def fill_matrix(X: np.ndarray, mixture: GaussianMixture) -> np.ndarray:
    """Fills an incomplete matrix according to a mixture model

    Args:
        X: (n, d) array of incomplete data (incomplete entries =0)
        mixture: a mixture of gaussians

    Returns
        np.ndarray: a (n, d) array with completed data
    """
    raise NotImplementedError

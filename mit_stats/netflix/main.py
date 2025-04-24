import numpy as np
import kmeans
import common
import naive_em
import em

X = np.loadtxt("toy_data.txt")

# Values of K and seeds to try
K_values = [1, 2, 3, 4]
seeds = [0, 1, 2, 3, 4]

# K-means run
# Iterate over each K
# for K in K_values:
#     best_cost = float('inf')
#     best_mixture = None
#     best_post = None
#     best_seed = None

#     # Try different seeds for initialization
#     for seed in seeds:
#         mixture, post = common.init(X, K, seed=seed)
#         mixture, post, cost = kmeans.run(X, mixture, post)
#         print(f"K={K}, Seed {seed}: Cost={cost:.2f}")

#         # Keep track of the best solution for this K
#         if cost < best_cost:
#             best_cost = cost
#             best_seed = seed
#             best_mixture = mixture
#             best_post = post

#     # Plot the best solution for this K
#     title = f"Best solution for K={K}, Seed = {best_seed} (Cost={best_cost:.2f})"
#     save_path = f"kmeans_best_K{K}_seed{best_seed}.png"
#     common.plot(X, best_mixture, best_post, title=title, save_path=None)

# # naive EM run
# for K in K_values:
#     best_em_cost = float('-inf')
#     best_em_mixture = None
#     best_em_post = None

#     for seed in seeds:
#         # Initialize and run EM
#         em_mixture, em_post = common.init(X, K, seed)
#         em_mixture, em_post, em_cost = naive_em.run(X, em_mixture, em_post)

#         print(f"EM: K={K}, Seed={seed}, Log-Likelihood={em_cost:.2f}")

#         # Keep track of the best EM solution
#         if em_cost > best_em_cost:
#             best_em_cost = em_cost
#             best_em_mixture = em_mixture
#             best_em_post = em_post

#     # Plot the best EM solution
#     title = f"Best EM solution for K={K} (Log-Likelihood={best_em_cost:.2f})"
#     save_path= f"em_best_K{K}.png"
#     common.plot(X, best_em_mixture, best_em_post, title=title, save_path=None)

# BIC run
best_K = None
best_bic = float('-inf')  # Initialize with a very low value
best_em_mixture = None
best_em_post = None

# Iterate over each K
for K in K_values:
    best_em_cost = float('-inf')
    best_em_mixture_for_K = None
    best_em_post_for_K = None

    # Try different seeds for initialization
    for seed in seeds:
        # Initialize and run EM
        em_mixture, em_post = common.init(X, K, seed)
        em_mixture, em_post, em_cost = naive_em.run(X, em_mixture, em_post)

        # Keep track of the best EM solution for this K
        if em_cost > best_em_cost:
            best_em_cost = em_cost
            best_em_mixture_for_K = em_mixture
            best_em_post_for_K = em_post

    # Compute BIC for the best EM solution for this K
    bic_value = common.bic(X, best_em_mixture_for_K, best_em_cost)
    print(f"K={K}, BIC={bic_value:.2f}")

    # Update the best K based on BIC
    if bic_value > best_bic:
        best_bic = bic_value
        best_K = K
        best_em_mixture = best_em_mixture_for_K
        best_em_post = best_em_post_for_K

# Report the best K and corresponding BIC score
print(f"Best K: {best_K}, Best BIC: {best_bic:.2f}")
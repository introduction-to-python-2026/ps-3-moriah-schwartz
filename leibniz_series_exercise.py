def approximate_pi(n_terms):
    approx_pi = 0.0

    for i in range(n_terms):
        approx_pi += ((-1) ** i) / (2 * i + 1)

    return 4 * approx_pi

def approximate_pi(n_terms):

 leibniz_series = []

 for i in range(n_terms):
    sign = (-1)**i
    denominator = 2 * i + 1
    term = sign * (1 / denominator)
    leibniz_series.append(term)

 leibniz_series_sum = sum(leibniz_series)
 approx_pi = 4*leibniz_series_sum

 return approx_pi

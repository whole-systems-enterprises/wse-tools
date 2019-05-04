
#
# import useful libraries
#
from numpy import percentile
from numpy.random import choice

#
# bootstrap (with no for loops). Works for a 1D array
#
# The "function" argument is something like np.mean, np.median, or np.std.
#
def bootstrap_1D_no_for_loops(x, function, repetitions, number_to_sample_with_replacement = None, confidence_interval_as_proportion = 0.95):
    if number_to_sample_with_replacement == None:
        number_to_sample_with_replacement = len(x)
    bootstrap_samples = choice(x, size = (number_to_sample_with_replacement, repetitions))
    function_applied_to_each_bootstrap_sample = function(bootstrap_samples, axis=0)
    function_applied_to_each_bootstrap_sample.sort()

    lower_bounds = (100. - (100. * confidence_interval_as_proportion)) / 2.
    upper_bounds = 100. - lower_bounds
    confidence_interval = percentile(function_applied_to_each_bootstrap_sample, [lower_bounds, upper_bounds])

    return function_applied_to_each_bootstrap_sample, confidence_interval

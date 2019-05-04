
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
# Assumes IID observations (e.g. no autocorrelation).
#
def bootstrap_1D_no_for_loops(x, function, repetitions, number_to_sample_with_replacement = None, confidence_interval_as_proportion = 0.95):

    # decide whether each resampled set should be as large as the original sample set
    if number_to_sample_with_replacement == None:
        number_to_sample_with_replacement = len(x)

    # draw n = repetitions number of bootstrap samples 
    bootstrap_samples = choice(x, size = (number_to_sample_with_replacement, repetitions))

    # apply the function to each repetition and sort the resulting 1D array
    function_applied_to_each_bootstrap_sample = function(bootstrap_samples, axis=0)
    function_applied_to_each_bootstrap_sample.sort()

    # compute confidence interval
    lower_bounds = (100. - (100. * confidence_interval_as_proportion)) / 2.
    upper_bounds = 100. - lower_bounds
    confidence_interval = percentile(function_applied_to_each_bootstrap_sample, [lower_bounds, upper_bounds])

    # return results
    return function_applied_to_each_bootstrap_sample, confidence_interval

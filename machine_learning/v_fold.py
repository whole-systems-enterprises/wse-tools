
import numpy as np
from itertools import combinations

def randomly_separate_indices_into_folds(N, n_folds):
    index_array = np.arange(0, N, 1, dtype=np.int64)
    np.random.shuffle(index_array)

    each_group_distance = int(round(float(N) / float(n_folds)))

    folds = np.zeros([n_folds, each_group_distance], dtype=np.int64)
    old_i = 0
    for index, i in enumerate(np.arange(0, n_folds * each_group_distance, each_group_distance, dtype=int)[1:]):
        folds[index] = index_array[old_i:i]
        old_i = i
    folds[index + 1] = index_array[i:(i + each_group_distance)]
    return folds

def get_the_v_fold_training_and_testing_indices(folds):
    n_folds = folds.shape[0]
    elements_per_fold = folds.shape[1]
    index_list = range(0, n_folds)
    training_indices = np.zeros([n_folds, (n_folds - 1) * elements_per_fold])
    testing_indices = np.zeros([n_folds, elements_per_fold])
    for idx, c in enumerate(combinations(index_list, n_folds - 1)):
        for testing_i in index_list:
            if not testing_i in c:
                break
        training_indices[idx] = folds[c, :].reshape([(n_folds - 1) * elements_per_fold])
        testing_indices[idx] = folds[testing_i, :]

    return training_indices, testing_indices







if __name__ == '__main__':
    folds = randomly_separate_indices_into_folds(100, 5)
    training_indices, testing_indices = get_the_v_fold_training_and_testing_indices(folds)

    print()
    print(training_indices)
    print()
    print(testing_indices)
    print()

    

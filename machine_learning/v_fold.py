
import numpy as np
from itertools import combinations

def separate_indices_into_folds(N, n_folds):
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
    training_list = []
    for c in combinations(index_list, n_folds - 1):
        for testing_i in index_list:
            if not testing_i in c:
                break
        training_indices = folds[c, :].reshape([(n_folds - 1) * elements_per_fold])
        training_list.append(training_indices)

    return training_list







if __name__ == '__main__':
    folds = separate_indices_into_folds(101, 5)
    training_list = get_the_v_fold_training_and_testing_indices(folds)

    print()
    print(training_list)
    print()
    print()
    print()

    

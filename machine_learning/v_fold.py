
import numpy as np

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








if __name__ == '__main__':
    print(separate_indices_into_folds(101, 5))

    
    


import numeric_tables

import pprint as pp
import numpy as np

if __name__ == '__main__':
    
    M = np.random.rand(3, 3)
    top_header = ['A', 'B', 'C']
    side_header = ['X', 'Y', 'Z']

    print()
    print(M)
    print()
    pp.pprint(numeric_tables.make_table_components_from_matrix(M, top_header, side_header=side_header))
    print()

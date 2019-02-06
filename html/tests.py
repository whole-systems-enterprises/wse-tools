
import numeric_tables

import pprint as pp
import numpy as np

if __name__ == '__main__':
    
    M = np.random.rand(3, 3)
    top_header = ['A', 'B', 'C']
    side_header = ['X', 'Y', 'Z']

    css = numeric_tables.make_generic_matrix_table_css()
    print(css)

    html = numeric_tables.make_table_from_matrix(M, top_header, side_header=side_header, round_it_to=3)
    f = open('output/html.html', 'w')
    f.write('<html><head><style>\n' + css + '\n</style></head><body>\n')
    f.write(html + '\n')
    f.write('</body></html>\n')
    f.close()


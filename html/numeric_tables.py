

def make_table_components_from_matrix(m, top_header, side_header=None, round_it_to=None):

    matrix_as_html_list = []

    #
    # top header
    #
    row_as_html_list = ['<tr class="wse-matrix-table-tr">']
    if side_header != None:
        row_as_html_list.append('<th class="wse-matrix-table-th"></th>')
    for header in top_header:
        row_as_html_list.append('<th class="wse-matrix-table-th">' + header + '</th>')
    row_as_html_list.append('</tr>')
    matrix_as_html_list.append(row_as_html_list)

    #
    # data
    #
    for i_idx, i in enumerate(m):
        row_as_html_list = ['<tr class="wse-matrix-table-tr">']
        
        if side_header != None:
            row_as_html_list.append('<th class="wse-matrix-table-th">' + side_header[i_idx] + '</th>')

        for j_idx, j in enumerate(i):
            post_round_j = j
            if round_it_to != None:
                post_round_j = round(j, round_it_to)
            row_as_html_list.append('<td class="wse-matrix-table-td">' + str(post_round_j) + '</td>')
        row_as_html_list.append('</tr>')
        matrix_as_html_list.append(row_as_html_list)

    return matrix_as_html_list


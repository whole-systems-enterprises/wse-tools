

def make_table_components_from_matrix(m, top_header, side_header=None, round_it_to=None, class_name_root='wse-matrix-table'):

    matrix_as_html_list = []

    #
    # top header
    #
    row_as_html_list = ['<tr class="' + class_name_root + '-tr">']
    if side_header != None:
        row_as_html_list.append('<th class="' + class_name_root + '-th"></th>')
    for header in top_header:
        row_as_html_list.append('<th class="' + class_name_root + '-th">' + header + '</th>')
    row_as_html_list.append('</tr>')
    matrix_as_html_list.append(row_as_html_list)

    #
    # data
    #
    for i_idx, i in enumerate(m):
        row_as_html_list = ['<tr class="' + class_name_root + '-tr">']
        
        if side_header != None:
            row_as_html_list.append('<th class="' + class_name_root + '-th">' + side_header[i_idx] + '</th>')

        for j_idx, j in enumerate(i):
            post_round_j = j
            if round_it_to != None:
                post_round_j = round(j, round_it_to)
            row_as_html_list.append('<td class="' + class_name_root + '-td">' + str(post_round_j) + '</td>')
        row_as_html_list.append('</tr>')
        matrix_as_html_list.append(row_as_html_list)

    return matrix_as_html_list


def make_table_from_matrix(m, top_header, side_header=None, round_it_to=None, class_name_root='wse-matrix-table'):
    matrix_as_html_list = make_table_components_from_matrix(m, top_header, side_header=side_header, round_it_to=round_it_to, class_name_root=class_name_root)

    html_as_list = []
    html_as_list.append('<div class="' + class_name_root + '-div">')
    html_as_list.append('<table class="' + class_name_root + '-table">')
    for row in matrix_as_html_list:
        for j in row:
            html_as_list.append(j)
    html_as_list.append('</table>')
    html_as_list.append('</div>')

    return '\n'.join(html_as_list)


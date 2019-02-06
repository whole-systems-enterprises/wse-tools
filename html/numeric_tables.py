"""
Functions for displaying numeric information in HTML
"""

#
# Used internally by the function "make_table_from_matrix"
#
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

#
# Creates an HTML display of a matrix
#
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

#
# makes a generic CSS template
#
def make_generic_matrix_table_css(class_name_root='wse-matrix-table'):
    css = ''
    css += '.' + class_name_root + '-table {\n'
    css += '  border-collapse: collapse;\n'
    css += '}'
    css += '\n'
    css += '.' + class_name_root + '-table, .' + class_name_root + '-th, .' + class_name_root + '-td {\n'
    css += '  border: 1px solid black;\n'
    css += '}'
    css += '\n'
    css += '.' + class_name_root + '-th, .' + class_name_root + '-td {\n'
    css += '  padding-left: 10px;\n'
    css += '  padding-right: 10px;\n'
    css += '}'
    return css

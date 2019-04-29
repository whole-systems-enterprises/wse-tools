import numpy as np

#
# A multiclass random forest regression in 
#

# [array([[0.69574713, 0.30425287],
#        [0.69796663, 0.30203337],
#        [0.68883045, 0.31116955],
#        ...,
#        [0.68484341, 0.31515659],
#        [0.69069149, 0.30930851],
#        [0.70113079, 0.29886921]]), array([[0.6290329 , 0.3709671 ],
#        [0.62713315, 0.37286685],
#        [0.62509155, 0.37490845],
#        ...,
#        [0.63890765, 0.36109235],
#        [0.63402011, 0.36597989],
#        [0.62436812, 0.37563188]]), array([[0.67521997, 0.32478003],
#        [0.67490022, 0.32509978],
#        [0.68607801, 0.31392199],
#        ...,
#        [0.67624894, 0.32375106],
#        [0.6752884 , 0.3247116 ],
#        [0.6745011 , 0.3254989 ]])]

# [[0.30425287 0.3709671  0.32478003]
#  [0.30203337 0.37286685 0.32509978]
#  [0.31116955 0.37490845 0.31392199]
#  ...
#  [0.31515659 0.36109235 0.32375106]
#  [0.30930851 0.36597989 0.3247116 ]
#  [0.29886921 0.37563188 0.3254989 ]]


def multiclass_random_forest_classifier_output_format_to_label_binarize_format(y_predicted, number_of_classes):
    nrows = y_predicted[0].shape[0]
    ncols = number_of_classes
    binarized_format = np.zeros([nrows, ncols])
    for i in range(number_of_classes):
        binarized_format[:, i] = y_predicted[i][:, 1]
    return binarized_format


"""
Dataframes usually are better, but these functions are helpful:
"""

#
# given two lists of equal length, where one contains a class indicator and the other contains the corresponding value, this function creates a dictionary where the classes are keys
#
def convert_class_and_item_lists_to_dict_with_classes_as_keys(class_list, item_list):
    new_dict = {}
    for group, item in zip(class_list, item_list):
        if not group in new_dict:
            new_dict[group] = []
        new_dict[group].append(item)
    return new_dict

#
# given two lists of equal length, where one contains a class indicator and the other contains the corresponding value, this function creates a list in the format required by Matplotlib's boxplot function (plus the labels). Also this format is good for scipy's Kruskal-Wallis test and ANOVA
#
def convert_class_and_items_lists_to_list_of_lists(class_list, item_list):
    dict_format = convert_class_and_item_lists_to_dict_with_classes_as_keys(class_list, item_list)
    labels_list = sorted(list(dict_format.keys()))
    new_list = []
    for key in labels_list:
        new_list.append(dict_format[key])
    return new_list, labels_list


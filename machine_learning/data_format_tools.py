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


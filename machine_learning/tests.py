import data_format_tools

import pprint as pp
import matplotlib.pyplot as plt

if __name__ == '__main__':

    class_list = [0, 1, 0, 1, 0, 1]
    item_list = [10, 10.5, 10.2, 10.6, 10.1, 10.55]

    the_dict = data_format_tools.convert_class_and_item_lists_to_dict_with_classes_as_keys(class_list, item_list)

    pp.pprint(the_dict)


    two_lists, labels_list = data_format_tools.convert_class_and_items_lists_to_boxplot_format(class_list, item_list)
    plt.figure()
    plt.boxplot(two_lists, widths=0.95)
    plt.xticks(range(1, len(labels_list) + 1), labels_list)
    plt.show()
    plt.close()


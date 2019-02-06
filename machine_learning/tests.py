import data_format_tools
import display

import pprint as pp
import matplotlib.pyplot as plt
from scipy.stats import kruskal
import random

if __name__ == '__main__':

    class_list = [0, 1, 0, 1, 0, 1, 2, 2]
    item_list = [10, 10.5, 10.2, 10.6, 10.1, 10.55, 11.1, 11.0]

    the_dict = data_format_tools.convert_class_and_item_lists_to_dict_with_classes_as_keys(class_list, item_list)

    pp.pprint(the_dict)


    list_of_lists, labels_list = data_format_tools.convert_class_and_items_lists_to_list_of_lists(class_list, item_list)

    print(kruskal(*list_of_lists))

#     plt.figure()
#     plt.boxplot(list_of_lists, widths=0.95)
#     plt.xticks(range(1, len(labels_list) + 1), labels_list)
#     plt.show()
#     plt.close()



    random.seed(23423)
    y_known = [1] * 100
    y_score = [random.gauss(0.4, 0.05) for x in range(0, 100)]
    y_known.extend([0] * 100)
    y_score.extend([random.gauss(0.3, 0.05) for x in range(0, 100)])

    display.make_roc_curve(y_known, y_score, title='ROC Curve Test')


    

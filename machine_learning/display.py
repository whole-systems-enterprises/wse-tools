from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

#
# Makes ROC curves
#
# Code modified from that at https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html.
#
def make_roc_curve(y_known, y_score, figsize=None, title='ROC Curve', filename=None):
    fpr, tpr, _ = roc_curve(y_known, y_score)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=figsize)
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")

    if filename == None:
        plt.show()
    else:
        plt.savefig(filename)

    plt.close()

    return roc_auc

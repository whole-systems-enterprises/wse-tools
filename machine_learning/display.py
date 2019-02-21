from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

#
# get ROC curve data
#
def get_roc_curve_data(y_known, y_score):
    fpr, tpr, _ = roc_curve(y_known, y_score)
    roc_auc = auc(fpr, tpr)
    return fpr, tpr, roc_auc

#
# plot ROC curve
#
# Code modified from that at https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html.
#
def plot_roc_curve(y_known, y_score, figsize=None, title='ROC Curve', filename=None):

    get_roc_curve_data(y_known, y_score)
    
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


#
# plot loss and metric
#
def plot_loss_and_metric(metric, history, loss_and_metric_filename):

    history_dict = history.history
    
    loss_values = history_dict['loss']
    val_loss_values = history_dict['val_loss']
    metric_values = history_dict[metric]
    val_metric_values = history_dict['val_' + metric]

    epochs = range(1, len(loss_values) + 1)

    plt.figure(figsize=[10, 12])

    plt.subplot(2, 1, 1)
    plt.plot(epochs, loss_values, 'bo', label='Training Loss')
    plt.plot(epochs, val_loss_values, 'b', label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(epochs, metric_values, 'bo', label='Training Metric')
    plt.plot(epochs, val_metric_values, 'b', label='Validation Metric')
    plt.title('Training and Validation Metric')
    plt.xlabel('Epochs')
    plt.ylabel('Metric')
    plt.legend()

    plt.savefig(loss_and_metric_filename)
    plt.close()

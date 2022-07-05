def get_classification_parameters(TN, TP, FN, FP):
    Acc = (TN + TP) / (TN + TP + FN + FP)
    Preс = TP / (TP + FP)
    Rec = TP / (TP + FN)
    print('Accuracy: {0}\n Precision: {1}\n Recall: {2}'.format(Acc, Preс, Rec))
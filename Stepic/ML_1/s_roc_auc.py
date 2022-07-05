#Площадь под ROC-кривой (величина AUC)

from sklearn.metrics import roc_auc_score

roc_auc_score([1,1,0,1,0,0], [0.6,0.81,0.5,0.9,0.7,0.75])
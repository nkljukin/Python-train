import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import sklearn.metrics
import itertools



data = pd.read_excel('Grains.xlsx', sheet_name = 'Grains', header = 0, usecols = 'B:I')


model = LinearRegression()

X = data[['Irrig', 'IrrigPrt', 'Nitr', 'Phos', 'Kali', 'Fallow', 'GrnsSq']]
X = sm.add_constant(X) #добавляет константу в коэффициенты уравнения
y = data[['GrnsYield']]
mod = model.fit(X,y)

result = sm.OLS(y, X).fit()


#print(data.describe())

#print("a = ", model.coef_)
#print("b = ", model.intercept_)
#print("R2 = ", model.score(X,y))

print(result.summary())

      
Beta = result.summary2().tables[1]['Coef.']
P_value = result.summary2().tables[1]['P>|t|']


df = pd.concat((Beta, P_value), axis=1).rename(columns={'Coef.': 'beta', 'P>|t|': 'P_value'})

print(df)



tr = pd.DataFrame({
    "Статистика": ["R2", "R2 adj.", "F-statistic", "P value", "К мульткол."],
    "Значение": [result.rsquared, result.rsquared_adj, result.fvalue, result.f_pvalue, result.condition_number],
        })
print(tr)


df.to_excel('result_par_pval.xlsx', 'sheet1')

 



# таблица вариантов моделей отсортированных по показателю мультиколлинеарности
predictorcols = ['Irrig', 'IrrigPrt', 'Nitr', 'Phos', 'Kali', 'Fallow', 'GrnsSq']
ConN = {}
for k in range(1, len(predictorcols)+1):    
    for variables in itertools.combinations(predictorcols, k):        
        predictors = X[list(variables)]
        predictors2 = sm.add_constant(predictors)
        est = sm.OLS(y, predictors2)
        res = est.fit()
        ConN[variables] = res.condition_number






    

 


#corr.to_excel(xlwriter, sheet_name = 'Info', index=True, startrow = 3, startcol = 0)
#descr.to_excel(xlwriter, sheet_name = 'Info', index=True, startrow = 15, startcol = 0)
#xlwriter.close()
#result.to_excel('Grains_res.xlsx', 'sheet1')
#xlwriter = pd.ExcelWriter('Grains_1.xlsx')







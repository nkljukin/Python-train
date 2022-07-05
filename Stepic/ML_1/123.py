import pandas as pd

data=pd.DataFrame({'U':[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],'V':[0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1],
                   'W':[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],'X':[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], 
                   'Y':[0,0.45,0.4,0.76,0.5,0.65,0.7,0.75,0.3,0.65,0.7,0.76,0.6,0.8,0.71,0.7]})

data['S']=data.iloc[:,0:4].sum(axis=1)
data.sort_values(by='S')

s1=data[(data['S']==1)][data['Y']==(data[(data['S']==1)]['Y'].max())]
i1=s1.iloc[0,0:4][s1.iloc[0,0:4]==1].index
print(s1, '\n', i1, '\n',len(i1))

 

s2=data[(data['S']==2) & (data[i1[0]]==1)][data['Y']==data[(data['S']==2) & (data[i1[0]]==1)]['Y'].max()]
i2=s2.iloc[0,0:4][s2.iloc[0,0:4]==1].index
print(s2, '\n', i2, '\n',len(i2))

 

s3=data[(data['S']==3) & (data[i2[0]]==1) & (data[i2[1]]==1)][data['Y']==data[(data['S']==3) & (data[i2[0]]==1) 
                                                                           & (data[i2[1]]==1)]['Y'].max()]
i3=s3.iloc[0,0:4][s3.iloc[0,0:4]==1].index
print(s3, '\n', i3, '\n',len(i3))

 

s4=data[(data['S']==4) & (data[i3[0]]==1) & (data[i3[1]]==1) & (data[i3[2]]==1)]
print(s4)
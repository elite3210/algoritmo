from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


df = pd.read_csv('emision.csv',delimiter=',',skiprows=[1])
print(df)

x = df['Fecha']
y = df['Emision']
print(x)
print(y)
print(len(x))
z = []
for i in range(len(x)):
    z.append(0)
    z[i] += int(x[i])
print(z)
w = []
for i in range(len(y)):
    w.append(0)
    w[i] += round(y[i]+w[i-1],3)
print(w)
print('longitud z: ',len(z))
print('longitud w: ',len(w))
plt.xlabel('Tiempo')
plt.ylabel('Millones S/')
#plt.hist(y,rwidth=0.95)

sns.linplot(z,w)
sns.set()
plt.show()
ax = sns.lineplot(x="time", y="firing_rate",
             hue="coherence", style="choice",
                 hue_norm=LogNorm(), data=dots)
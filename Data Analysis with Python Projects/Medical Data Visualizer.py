import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#https://replit.com/@LuizSinx/boilerplate-medical-data-visualizer-2#medical_data_visualizer.py VERSÂO final
df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / ((df['height']/100) ** 2)).apply(lambda x: 1 if x > 25 else 0)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x <= 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x <= 1 else 1)

# Clean the data

df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]


grafico_diseas = df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight', 'cardio']]
grafico_diseas = grafico_diseas.melt(id_vars='cardio', var_name="varieble")


tabela = sns.catplot(data=grafico_diseas, x='varieble', kind='count', hue='value', col='cardio', order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
tabela.set(ylabel="total", xlabel='variable')
tabela = tabela.fig


# Calculate the correlation matrix
corr = df_heat.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr))

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 10))

# Draw the heatmap with 'sns.heatmap()'
ax = sns.heatmap(data=corr, mask=mask, square=True, annot=True, fmt='0.1f', center=0, vmax=.24, linewidths=.4, robust=True)


plt.show()
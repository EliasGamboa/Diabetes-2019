# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:28:36 2022

@author: saile
"""
import pandas as pd

diabetesbrz = ['Brasil', 16876.65]
diabetesind = ['India', 77005.77]
diabetesmx = ['Mexico', 12831.78]
diabetesch = ['China', 110500.94]
diabeteseu = ['EE.UU', 30998.00]
diabetespk = ['Paquistan', 19369.82]




lista_paisDiab = [diabetesch, diabetesind, diabeteseu, diabetespk, diabetesbrz, diabetesmx]
#crear dataframe a partir de listas
df_paisDiab = pd.DataFrame(lista_paisDiab, columns=['Pais', 'Cantidad'])
df_paisDiab

import matplotlib.pyplot as plt

plt.title('Cantidad de diabeticos en 2019')
#grafico de puntos
plt.scatter(df_paisDiab['Pais'], df_paisDiab['Cantidad'])
plt.show
#grafico lineal
plt.title('Cantidad de diabeticos en 2019')
plt.plot(df_paisDiab['Pais'], df_paisDiab['Cantidad'])
plt.show()
#grafico de barras
plt.title('Cantidad de diabeticos en 2019')
plt.bar(df_paisDiab['Pais'], df_paisDiab['Cantidad'])
plt.show
#grafico de barras ordenado y con color
plt.title('Cantidad de diabeticos en 2019')
df_paisDiab_sort=df_paisDiab.sort_values('Cantidad', ascending=False)
plt.bar(df_paisDiab['Pais'], df_paisDiab['Cantidad'], color=['b', 'r', 'g', 'm', 'k', 'c'])
plt.show
#grafico de puntos
plt.title('Cantidad de diabeticos en 2019')
plt.pie(df_paisDiab['Cantidad'], labels=df_paisDiab['Pais'], shadow=True, autopct='%1.1f%%')
plt.show
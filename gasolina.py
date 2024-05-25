# código de geração do gráfico
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('gasolina.csv')

grafico = sns.lineplot(data=data, x="dia", y="venda", ci=None, palette="pastel")
grafico.set(title='Preço da gasolina por dia', xlabel='dia', ylabel='preço')
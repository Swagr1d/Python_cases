import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('cadastral_numbers_list.csv', index_col='PassengerId', encoding='cp1251')
print(data)
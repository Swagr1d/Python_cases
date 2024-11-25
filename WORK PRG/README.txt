Добываем координаты по кадастровому номеру
1) получаем в отдельный столбец кадастровые из адресов [мой скрипт take_cad #]
2) собираем все кадастровые в txt по порядку
3.000) pip install rosreestr2coord
3) rosreestr2coord -С -l ./cadastral_numbers_list.txt
С — центрует координаты
l — принять данные ЛИСТ
terminal 
cd или cd ..
ls список папок
cd Desktop выбираем файл txt с координатами с рабочего стола, код пишет куда сохранил, на раб столе папка output
в окне код прописывай сохранить в xlsx файл и нажимай Shift+Enter и там уже разбивка будет по столбцам 
обновление pip
python -m pip install --upgrade pip
python -m pip install --upgrade rosreestr2coord

4) Jupyter Notebook открываем в Visual SC (плагин Jupyter)– создав файл с расширением .ipynb
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('cadastral_numbers_list.csv')
print(data)
df = pd.DataFrame(data)

# Очистка данных от лишних символов. Метод Replace заменит [[[[ и ]]]] ни на что
df = df.replace({r"\[\[\[\[|\]\]\]\]": ""}, regex=True) 

# Сохранение DataFrame в Excel: индекс false для разбивки по строкам
df.to_excel("coord_result_list.xlsx", index=False, engine="openpyxl")


в блоке кода и все сохраним результат с разбивкой берем координаты в наш перечень через ВПР


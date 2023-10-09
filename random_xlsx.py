# создает файл exel с 50000 рандомных 10ти значных чисел

import random
import pandas as pd

count = 0
data = []

while count != 50000:  # количесьво сгенерированых числед
    data.append(random.randint(0000000000, 9999999999))  # диапазон рандомных числед
    print(count)
    count += 1

df = pd.DataFrame(data, columns=['number'])  # название колонки
df.to_excel('test_exel_3.xlsx')  # имя создаваемого EXEL файла

print(df)

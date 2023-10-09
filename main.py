import pandas as pd
import glob
import time

start_time = time.time()

name_number = 'number'  # название столбца для пересечения

# создать интерфейс выбора папки в которой находятся файлы
# file_list = glob.glob('data_dir/*xlsx')


# сделать чтобы каждый фрейм создавался на находящийся в папке(file_list) xlsx фаил
df1 = pd.read_excel('test_exel_1.xlsx')  # файл по 500000 рандомных 10 цыфр
df2 = pd.read_excel('test_exel_2.xlsx')  # файл по 500000 рандомных 10 цыфр
df3 = pd.read_excel('test_exel_3.xlsx')  # файл по 500000 рандомных 10 цыфр

# оставляем только уникальные элементы
mylist1 = set(df1[name_number].tolist())
mylist2 = set(df2[name_number].tolist())
mylist3 = set(df3[name_number].tolist())

# написать функцию которая пресекает фреймы в зависимости от их количества
end_result = mylist1 & mylist2 & mylist3

print(end_result)

end_time = str(time.time() - start_time)[:-15] + ' сек'

print(end_time)

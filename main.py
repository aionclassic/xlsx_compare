import pandas as pd
import time
import os

name_column = 'number'  # название столбца для пересечения

#создает список файлов находящихся в папке переменная data_directory


#создаем переменные df_1...N с путями к N файлам из папки
list_file = []
data_directory = '111'
for root, dirs, files in os.walk(data_directory):
    for filename in files:
        list_file.append(os.path.join(root, filename))

#создаем преременную dfN с 1ё колонкой , создаем из этой переменно переменую с уникальными занчениями вколонке
ii=0
iii=[]
for i in list_file:
    ii += 1
    globals()[f'df{ii}'] = pd.read_excel(i)
    globals()[f'set_data_df{ii}'] = set(eval(f'df{ii}[name_column]'))
    iii.append(f'set_data_df{ii}')

start_time = time.time()

# функцию которая пресекает фреймы в зависимости от их количества
end_result =[]
for xxx in iii:
    end_result.extend(xxx+' &')

#удаляем последний элемент & и собираем в строку
end_result.pop(-1)
end_result_data=eval("".join(end_result))


print(end_result_data)


end_time = str(time.time() - start_time)[:-15] + ' сек'

print(end_time)
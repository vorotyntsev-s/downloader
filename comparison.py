import os
import wget

url = 'http://192.168.1.51:8081'

with open('revision_srv.txt') as file: #Читаем файл
    lines = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк

dic_srv = {} # Создаем пустой словарь

for line in lines: # Проходимся по каждой строчке
    key,value = line.split("  ") # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
    dic_srv.update({key:value})	 # Добавляем в словарь
x = dict(sorted(dic_srv.items()))



with open('revision_local.txt') as file: #Читаем файл
    lines = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк

dic_local = {} # Создаем пустой словарь

for line in lines: # Проходимся по каждой строчке
    key, value = line.split('  ') # Разделяем каждую строку по двум пробелам
    dic_local.update({key:value})	 # Добавляем в словарь
y = dict(sorted(dic_local.items()))


def operator_important(operator_one, operator_two):
    """Поиск одинаковых элементов в словаре и словаре и запись в словарь."""

    operator_main = dict()

    for key, value in operator_one.items():
        if key in operator_two and value == operator_two[key]:
            continue
        else:
            if os.path.isfile(f'.{value}'):
                os.remove(f'.{value}')
            wget.download(f'{url}{value}', out=f'.{value}')
            print(f'{url}{value}')


operator_important(x, y)



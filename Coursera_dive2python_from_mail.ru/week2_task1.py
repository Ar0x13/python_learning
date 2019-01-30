#!/usr/bin/env python
# ======== TASK DESCRIPTION ========
На этой неделе мы с вами реализуем собственный key-value storage. Вашей задачей будет написать скрипт, который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).
Запись значения по ключу
> storage.py --key key_name --val value
Получение значения по ключу
> storage.py --key key_name
Ответом в данном случае будет вывод с помощью print соответствующего значения
> value
или
> value_1, value_2
если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке их добавления. Обратите внимание на пробел после запятой.
Если значений по ключу не было найдено, выводите пустую строку или None.
Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей будет считать аргументы, переданные вашей программе, и записать соответствующую пару ключ-значение в файл хранилища или вывести значения, если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json. Проверьте добавление нескольких ключей и разных значений.
Файл следует создавать с помощью модуля tempfile.
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
  ...
# ======== END OF TASK DESCRIPTION ========

import os
import sys 
import argparse
import tempfile

parser = argparse.ArgumentParser(description='Key-value storage')
parser.add_argument('-k','--key', help='Storage key', required=True)
parser.add_argument('-v','--val', help='Key value')
args = parser.parse_args()
print(args.key)
print(args.val)


def read_tmp_file():
    print("Current temp directory:", tempfile.gettempdir())
    try:
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    except:
        print("Cannot find tmp file or folder!")

def insert_data(key, value):
	data = {}
	data[key]=value
	with open(storage_path, 'w') as f:
		f.write(json.dumps(data)) 


def print_data(key, value=None):
	with open(storage_path, 'w') as f:
		print(f.read)



def main():
    print("Number of arguments: ", len(sys.argv))
    print("Argument List: ", str(sys.argv))
    read_tmp_file()
    # if len(sys.argv) == 3:
    #     print_data()
    if len(sys.argv) == 5:
    	insert_data()

    
if __name__ == '__main__':
    main()

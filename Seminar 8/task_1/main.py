"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import re


def get_data():
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта",
                  "Тип системы"]]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for i in range(1, 4):
        try:
            with open(f"info_{i}.txt") as f:
                file_data = f.read()
                os_prod_match = re.search(r"Изготовитель системы:\s*(.*)",
                                          file_data)
                os_prod_list.append(os_prod_match.group(1).strip())
                os_name_match = re.search(r"Название ОС:\s*(.*)", file_data)
                os_name_list.append(os_name_match.group(1).strip())
                os_code_match = re.search(r"Код продукта:\s*(.*)", file_data)
                os_code_list.append(os_code_match.group(1).strip())
                os_type_match = re.search(r"Тип системы:\s*(.*)", file_data)
                os_type_list.append(os_type_match.group(1).strip())
        except FileNotFoundError:
            print(f"Файл info_{i}.txt не найден")
    for j in range(len(os_prod_list)):
        main_data.append([os_prod_list[j], os_name_list[j], os_code_list[j],
                          os_type_list[j]])
    return main_data


def write_to_csv(csv_file):
    data = get_data()
    with open(csv_file, mode='w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


write_to_csv("data_report.csv")

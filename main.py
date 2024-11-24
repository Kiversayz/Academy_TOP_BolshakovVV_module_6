import os
""" 
Задача 6.2.1

Для выполнения данного задания я настоятельно рекомендую
создать абсолютно новый проект.

В этом проекте вам необходимо создать 2 папки а в каждой из
них по 2 файла формата .txt:
data_path_1 файлы внутри test_file_1.txt, test_file_2.txt;
data_path_2 файлы внутри test_file_3.txt, test_file_4.txt.

В корневой папке проекта вам необходимо создать файл
main.py
В этом файле вам необходимо написать код, который должен
выполнять следующие задачи;

Указать в консоли нормализованный абсолютный путь к
файлу test_file_1.txt

1. При помощи функции os.walk() вывести в консоль
содержимое папки вашего нового проекта
2. При помощи метода os.path.join() cоставить
нормализованный абсолютный путь к файлу
test_file_3.txt
3. Написать код для создания и для удаления папки внутри
папки data_path_2
 """


# Указать в консоли нормализованный абсолютный путь к файлу test_file_1.txt
print(os.path.abspath(os.path.join('data_path_1', 'test_file_1.txt'))) #os.path.join(): Объединяет пути таким образом, который корректно работает на разных операционных системах (Windows, macOS, Linux).
#abspath преобразует относительный путь os.path.join('data_path_1', 'test_file_1.txt') в абсолютный /workspaces/Academy_TOP_BolshakovVV_module_6/data_path_1/test_file_1.txt


# 2. При помощи функции os.walk() вывести в консоль содержимое папки вашего нового проекта
for root, dirs, files in os.walk('.'): #os.walk('.') '.' - указываем на текущуюю деррикторию
    print(f"Папка: {root}")
    for dir in dirs:
        print(f"  Папка: {dir}")
    for file in files:
        print(f"  Файл: {file}")

# 3. При помощи метода os.path.join() составить нормализованный абсолютный путь к файлу test_file_3.txt
print(os.path.abspath(os.path.join('data_path_2', 'test_file_3.txt'))) 

# 4. Написать код для создания и для удаления папки внутри папки data_path_2
new_folder = 'new_folder'
new_folder_path = os.path.normpath(os.path.join('data_path_2', new_folder)) #os.path.normpath(): Нормализует путь, убирая лишние символы и делая его более читаемым.

try:
    # Создать папку
    os.mkdir(new_folder_path) #os.mkdir(path): Создает директорию. Вызывает ошибку FileExistsError, если директория уже существует.
    print(f"Папка {new_folder} создана")
except FileExistsError:
    print(f"Папка {new_folder} уже существует")

try:
    # Удалить папку
    os.rmdir(new_folder_path) #os.rmdir(path): Удаляет пустую директорию. Вызывает FileNotFoundError, если не существует.
    print(f"Папка {new_folder} удалена")
except FileNotFoundError:
    print(f"Папка {new_folder} не существует")

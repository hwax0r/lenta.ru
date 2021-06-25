
# Тестовое задание:
# Напишите скрипт на любом скриптовом языке, выдающий статистику по типам файлов на жестком диске.
# В качестве входного параметра скрипт получает имя каталога, с которого начинается поиск.
# Скрипт выводит на стандартный вывод расширение файла и количество найденных файлов такого типа.
# Список сортируется по убыванию.


import os

statistics = {}


def main_menu():
    path = input("\nВведите путь для анализа: ")
    if not os.path.exists(path):
        print("\n\tОшибка!\n\tТакого пути не существует.")
    return path


def extension(filename):
    file_name, file_extension = os.path.splitext(filename)
    return file_extension


def update_stats(file_extension):
    if file_extension == '':
        return
    if file_extension not in statistics.keys():
        statistics.update({file_extension: 0})
    statistics[file_extension] += 1


def walker(path):
    for current_path, folders, files in os.walk(path):
        for file in files:
            update_stats(extension(file))


def stats_output():
    for key, value in sorted(statistics.items(), key=lambda x: x[1], reverse=True):
        print("{}: {}".format(key, value))


def main():
    walker(main_menu())
    stats_output()


if __name__ == '__main__':
    main()

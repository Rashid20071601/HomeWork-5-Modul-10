# Импорт библиотек
from time import time
import multiprocessing


def read_info(name):
    all_data = []  # Инициализация списка для хранения данных
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()  # Чтение строки из файла
            if not line:  # Проверка на конец файла
                break
            all_data.append(line)  # Добавление строки в список


# Список имен файлов для обработки
filenames = [f'./file {number}.txt' for number in range(1, 5)]

'''
# Линейный вызов
start_time = time()  # Запуск таймера

for filename in filenames:
    read_info(filename)  # Чтение данных из каждого файла

end_time = time()  # Остановка таймера

print(f"Время выполнения линейного процесса: {round(end_time - start_time, 3)} секунд")
'''


# Многопроцессный вызов
if __name__ == '__main__':
    start_time = time()  # Запуск таймера

    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, filenames)  # Параллельное чтение файлов

    end_time = time()  # Остановка таймера

    print(f"Время выполнения многопроцессной обработки: {round(end_time - start_time, 3)} секунд")  # Вывод времени выполнения
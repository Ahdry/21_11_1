import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы
    # Вы можете сделать что-то с all_data, если нужно, но в данной задаче это не требуется

if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]  # Замените на ваши файлы

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"Линейный вызов: {linear_time}")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f"Многопроцессный вызов: {multiprocessing_time}")
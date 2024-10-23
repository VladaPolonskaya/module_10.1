from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for num_ in range(1, word_count + 1):
            file.write(f'Какое-то слово № {num_}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_1 = datetime.now()
record_1 = write_words(10, 'example1.txt')
record_2 = write_words(30, 'example2.txt')
record_3 = write_words(200, 'example3.txt')
record_4 = write_words(100, 'example4.txt')
time_2 = datetime.now()
print(f'Работа потоков: {time_2 - time_1}')
print()
time_3 = datetime.now()
args_1 = 10, 'example5.txt'
args_2 = (30, 'example6.txt')
args_3 = (200, 'example7.txt')
args_4 = (100, 'example8.txt')
thr_1 = Thread(target=write_words, args=args_1)
thr_2 = Thread(target=write_words, args=args_2)
thr_3 = Thread(target=write_words, args=args_3)
thr_4 = Thread(target=write_words, args=args_4)
thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()
thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
time_4 = datetime.now()
print(f'Работа потоков: {time_4 - time_3}')
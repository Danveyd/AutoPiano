import time
from pynput.keyboard import Controller, Key
import sys

# Проверяем, является ли символ допустимой клавишей
def is_valid_key(key):
    # Допустимые символы - можно расширять по мере необходимости
    valid_keys = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>?/`~ ")  
    return len(key) == 1 and key in valid_keys

# Функция для нажатия клавиш
def press_keys(keys):
    press_set = []  # Храним клавиши для одновременного нажатия

    for key in keys:
        if key.startswith('[') and key.endswith(']'):  # Клавиши внутри квадратных скобок
            key_name = key[1:-1]
            if True:#is_valid_key(key_name):  # Проверяем, допустимо ли нажатие этой клавиши
                for k in key_name:
                    press_set.append(k)  # Добавляем к списку для одновременного нажатия
        
        else:
            if is_valid_key(key):  # Проверяем на допустимость обычных ключей
                if key.isupper():  # Проверка на заглавные буквы
                    keyboard.press(Key.shift)
                    keyboard.press(key.lower())
                    keyboard.release(key.lower())
                    keyboard.release(Key.shift)
                else:
                    keyboard.press(key)
                    keyboard.release(key)

    # Нажимаем и отпускаем все клавиши из списка одновременно
    for k in press_set:
        keyboard.press(k)

    for k in press_set:
        keyboard.release(k)

def remove_newlines(input_string):
    # Удаляем символы новой строки и объединяем текст в одну строку
    return ' '.join(input_string.splitlines()).strip()


# Основная функция
def main():
    print("Enter the keys (you can use line breaks, finish with Ctrl+D on Unix or Ctrl+Z on Windows):")

    # Читаем весь ввод
    xz = sys.stdin.read()

    # Удаляем новые строки и выводим результат
    input_keys = remove_newlines(xz)
    
    # Добавляем обработку ввода времени задержки
    while True:
        delay_input = input("Enter the delay time between clicks in seconds: ")
        if delay_input.strip():  # Проверяем, что строка не пустая
            try:
                delay = float(delay_input)
                break  # Выходим из цикла, если преобразование прошло успешно
            except ValueError:
                print("Error: Please enter a valid number for the delay (eg 0.5).")
        else:
            print("Error: Input must not be empty. Please try again.")

    keys = input_keys.split()
    
    print("Get ready! It starts in 5 seconds...")
    time.sleep(5)  # Задержка перед началом

    for key in keys:
        press_keys([key])
        time.sleep(delay)

    print("The end")

if __name__ == "__main__":
    keyboard = Controller()
    main()

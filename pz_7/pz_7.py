# 1. Дана непустая строка. Вывести коды ее первого и последнего символа.

def task1():
    text = input("Введите строку: ")
    
    if len(text) == 0:
        print("Ошибка: строка пустая")
        return
    
    first_char_code = ord(text[0])
    last_char_code = ord(text[-1])
    
    print(f"Код первого символа '{text[0]}': {first_char_code}")
    print(f"Код последнего символа '{text[-1]}': {last_char_code}")

# 2. Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов (путь), собственно имя и расширение. 
#    Выделить из этой строки расширение файла (без предшествующей точки).

def task2():
    file_path = input("Введите полное имя файла: ")
    
    # Разделяем путь по точкам и берем последнюю часть
    parts = file_path.split('.')
    
    if len(parts) > 1:
        extension = parts[-1]
        print(f"Расширение файла: {extension}")
    else:
        print("Расширение не найдено")

def main():
    print("=== ЗАДАЧА 1 ===")
    task1()
    
    print("\n=== ЗАДАЧА 2 ===")
    task2()

if __name__ == "__main__":
    main()
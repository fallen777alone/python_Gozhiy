# Приложение АПТЕКА для автоматизации работы аптечных пунктов. Таблица
# Лекарственные Средства должна содержать следующую информацию: Код, Название
# препарата, Применение, Количество, Цена, Страна-производитель.

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Подключено к SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Лекарственные_Средства (
            Код INTEGER PRIMARY KEY AUTOINCREMENT,
            Название_препарата TEXT NOT NULL,
            Применение TEXT,
            Количество INTEGER NOT NULL,
            Цена REAL NOT NULL,
            Страна_производитель TEXT
        );
        """)
        print("Таблица 'Лекарственные_Средства' создана успешно")
    except Error as e:
        print(e)


def add_medication(conn, medication):
    sql = """INSERT INTO Лекарственные_Средства(Название_препарата, Применение, Количество, Цена, Страна_производитель)
              VALUES(?,?,?,?,?)"""
    cursor = conn.cursor()
    cursor.execute(sql, medication)
    conn.commit()
    return cursor.lastrowid


def update_medication(conn, medication):
    sql = """UPDATE Лекарственные_Средства
              SET Название_препарата = ?,
                  Применение = ?,
                  Количество = ?,
                  Цена = ?,
                  Страна_производитель = ?
              WHERE Код = ?"""
    cursor = conn.cursor()
    cursor.execute(sql, medication)
    conn.commit()


def delete_medication(conn, code):
    sql = "DELETE FROM Лекарственные_Средства WHERE Код = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (code,))
    conn.commit()


def select_all_medications(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Лекарственные_Средства")

    rows = cursor.fetchall()

    print("\nСписок всех лекарственных средств:")
    print("-" * 80)
    for row in rows:
        print(f"Код: {row[0]}")
        print(f"Название: {row[1]}")
        print(f"Применение: {row[2]}")
        print(f"Количество: {row[3]}")
        print(f"Цена: {row[4]} руб.")
        print(f"Страна-производитель: {row[5]}")
        print("-" * 80)


def search_medication(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Лекарственные_Средства WHERE Название_препарата LIKE ?", ('%' + name + '%',))

    rows = cursor.fetchall()

    if len(rows) > 0:
        print("\nРезультаты поиска:")
        print("-" * 80)
        for row in rows:
            print(f"Код: {row[0]}")
            print(f"Название: {row[1]}")
            print(f"Применение: {row[2]}")
            print(f"Количество: {row[3]}")
            print(f"Цена: {row[4]} руб.")
            print(f"Страна-производитель: {row[5]}")
            print("-" * 80)
    else:
        print("Лекарства с таким названием не найдены.")


def main():
    database = "apteka.db"

    conn = create_connection(database)

    if conn is not None:
        create_table(conn)

        while True:
            print("\nАПТЕКА - система управления аптечным пунктом")
            print("1. Добавить новое лекарство")
            print("2. Просмотреть все лекарства")
            print("3. Поиск лекарства по названию")
            print("4. Обновить информацию о лекарстве")
            print("5. Удалить лекарство")
            print("6. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                name = input("Название препарата: ")
                usage = input("Применение: ")
                quantity = int(input("Количество: "))
                price = float(input("Цена: "))
                country = input("Страна-производитель: ")

                medication = (name, usage, quantity, price, country)
                add_medication(conn, medication)
                print("Лекарство успешно добавлено!")

            elif choice == "2":
                select_all_medications(conn)

            elif choice == "3":
                name = input("Введите название препарата для поиска: ")
                search_medication(conn, name)

            elif choice == "4":
                code = int(input("Введите код лекарства для обновления: "))
                name = input("Новое название препарата: ")
                usage = input("Применение: ")
                quantity = int(input("Количество: "))
                price = float(input("Цена: "))
                country = input("Страна-производитель: ")

                medication = (name, usage, quantity, price, country, code)
                update_medication(conn, medication)
                print("Информация о лекарстве обновлена!")

            elif choice == "5":
                code = int(input("Введите код лекарства для удаления: "))
                delete_medication(conn, code)
                print("Лекарство удалено из базы данных!")

            elif choice == "6":
                print("Выход из программы...")
                break

            else:
                print("Неверный ввод. Пожалуйста, выберите действие от 1 до 6.")

        conn.close()
    else:
        print("Ошибка! Не удалось подключиться к базе данных.")


if __name__ == '__main__':
    main()
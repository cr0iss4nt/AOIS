from hash_table_class import hash_table_from_terms, table_term
from hash_table_functions import normalize_term_name
from terms_biology import terms_biology

table = hash_table_from_terms(terms_biology)

print("Здравствуйте!")
while True:
    choice = input("""
1) Вывод таблицы
2) Поиск строки по ключу
3) Добавление строки по ключу
4) Удаление строки по ключу
0) Выход
Ваш выбор: """)

    match choice:
        case '1':
            print('')
            print(table)

        case '2':
            key = normalize_term_name(input("Введите ключ: "))
            definition = table.get(key)
            if definition is None:
                print("Определения термина в таблице нет.")
            else:
                print(table_term(table, key))

        case '3':
            term = normalize_term_name(input("Введите термин: "))
            definition = table.get(term)
            if definition is None:
                definition = input("Введите определение: ")
                table.set(term, definition)
                print("Термин был успешно добавлен!")
            else:
                print("Данный термин уже определён в таблице:")
                print(table_term(table, term))

        case '4':
            term = normalize_term_name(input("Введите термин: "))
            if not table.delete(term):
                print("Такого термина в таблице и не было.")
            else:
                print("Термин был успешно удалён!")

        case '0':
            print("До свидания!")
            break

        case _:
            print("Неверный ввод!")

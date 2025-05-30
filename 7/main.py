from matrix_class import Matrix

matrix = Matrix()
while True:
    print("Матрица:")
    matrix.output()
    choice = input("""1) Получить слово
2) Перезаписать слово
3) Получить разрядный столбец
4) Перезаписать разрядный столбец
5) Произвести логическую операцию над разрядными столбцами
6) Поиск по соответствию
7) Сложение полей в словах с заданным V
0) Выход
Ваш выбор: """)
    match choice:
        case '1':
            try:
                word_number = int(input("Введите номер слова (0-15): "))
                word = matrix.get_word(word_number)
                print(f"Слово {word_number}:")
                print(word)
            except ValueError:
                print("Неверный ввод!")

        case '2':
            try:
                word_number = int(input("Введите номер слова (0-15): "))
                word = input("Введите слово (длиной 16): ")
                matrix.replace_word(word_number,word)
                print("Слово было успешно заменено!")
            except ValueError:
                print("Неверный ввод!")

        case '3':
            try:
                diagonal_number = int(input("Введите номер разрядного столбца (0-15): "))
                diagonal = matrix.get_diagonal(diagonal_number)
                print(f"Разрядный столбец {diagonal_number}:")
                print(diagonal)
            except ValueError:
                print("Неверный ввод!")

        case '4':
            try:
                diagonal_number = int(input("Введите номер разрядного столбца (0-15): "))
                diagonal = input("Введите слово (длиной 16): ")
                matrix.replace_diagonal(diagonal_number, diagonal)
                print("Разрядный столбец был успешно заменён!")
            except ValueError:
                print("Неверный ввод!")

        case '5':
            try:
                diagonal1_number = int(input("Введите номер первого разрядного столбца (0-15): "))
                diagonal2_number = int(input("Введите номер второго разрядного столбца (0-15): "))
                result_diagonal_number = int(input("Введите номер разрядного столбца для записи результатов (0-15): "))
                function_number = input("Введите номер функции (0, 5, 10, 15): ")

                matrix.logic(diagonal1_number, diagonal2_number, result_diagonal_number,function_number)
                print("Логическая операция была успешно применена!")
            except ValueError:
                print("Неверный ввод!")

        case '6':
            try:
                argument = input("Введите аргумент поиска (двоичное число): ")

                best_candidate_index, max_matches = matrix.search_by_match(argument)
                if best_candidate_index == -1:
                    print("Совпадений нет.")
                else:
                    print(f"Наилучшее совпадение: слово {best_candidate_index}")
                    print(f"Количество совпадений: {max_matches}")
            except ValueError:
                print("Неверный ввод!")

        case '7':
            try:
                argument = input("Введите V: ")

                matrix.summarize_words(argument)
                print("Таблица была успешно обработана!")
            except ValueError:
                print("Неверный ввод!")

        case '0':
            print("До свидания!")
            break

        case _:
            print("Неверный ввод!")

    print('')
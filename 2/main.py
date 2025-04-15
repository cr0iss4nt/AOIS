from formula import normalize
from number_functions import index_form, number_perfect_conjunctive_normal_form, number_perfect_disjunctive_normal_form
from perfect_normal_form import build_perfect_conjunctive_normal_form, build_perfect_disjunctive_normal_form
from truth_table import TruthTable

while True:
    formula = input("Введите формулу: ")
    formula = normalize(formula)
    print(formula)

    truth_table = TruthTable(formula)
    print("Таблица истинности:")
    truth_table.output()

    print("СКНФ:", build_perfect_conjunctive_normal_form(formula))
    print("Числовая форма СКНФ:", number_perfect_conjunctive_normal_form(formula))
    print("СДНФ:", build_perfect_disjunctive_normal_form(formula))
    print("Числовая форма СДНФ:", number_perfect_disjunctive_normal_form(formula))

    print("Индексная форма формулы:", index_form(formula))

    print('')
    while True:
        choice = input("Хотите ли вы ввести ещё одну формулу? (y/n) ")
        match choice.lower():
            case 'y':
                break
            case 'n':
                print("До свидания!")
                exit()
            case _:
                print("Неверный ввод!")

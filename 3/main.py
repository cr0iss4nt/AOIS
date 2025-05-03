from formula import normalize
from minimization_gluing import minimize_implicant_check, minimize_chart
from minimization_karnaugh import minimize_karnaugh
from perfect_normal_form import build_perfect_disjunctive_normal_form, build_perfect_conjunctive_normal_form

while True:
    formula = input("Введите формулу: ")
    print("")

    formula = normalize(formula)
    sdnf = build_perfect_disjunctive_normal_form(formula)
    print("СДНФ:", sdnf, "\n")
    sdnf_rasch = minimize_implicant_check(sdnf, is_conjunction=False)
    print("Расчётный метод:", sdnf_rasch, "\n")
    sdnf_rasch_tabl = minimize_chart(sdnf, is_conjunction=False)
    print("Расчётно-табличный метод:", sdnf_rasch_tabl, "\n")
    sdnf_karnaugh = minimize_karnaugh(sdnf, is_conjunction=False)
    print("Табличный метод:", sdnf_karnaugh, "\n\n\n")

    sknf = build_perfect_conjunctive_normal_form(formula)
    print("СКНФ:", sknf, "\n")
    sknf_rasch = minimize_implicant_check(sknf, is_conjunction=True)
    print("Расчётный метод:", sknf_rasch, "\n")
    sknf_rasch_tabl = minimize_chart(sknf, is_conjunction=True)
    print("Расчётно-табличный метод:", sknf_rasch_tabl, "\n")
    sknf_karnaugh = minimize_karnaugh(sknf, is_conjunction=True)
    print("Табличный метод:", sknf_karnaugh, "\n\n\n")

    while True:
        choice = input("Хотите ли вы ввести ещё одну формулу? (y/n) ")
        match choice.lower():
            case 'y':
                break
            case 'n':
                print("До свидания!")
                exit(0)
            case '_':
                print("Неверный ввод!")

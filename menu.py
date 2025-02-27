import sys
import time
import msvcrt

from algorithmChecker import algorithmChecker


class menu:
    def start_menu(self):
        flag = True

        while(flag):
            try:
                answer = int(input(
                            "Выберите функцию:\n"
                            "1. Проверка номера карты на подлинность.\n"
                            "2. Найти недостающую цифру номера карты.\n"
                            "3. Вики.\n"
                            "4. Выход.\n"))
                if answer == 1:
                    self.__check_menu()
                    flag = False
                elif answer == 2:
                    self.__edit_num_menu()
                    flag = False
                elif answer == 3:
                    self.__wiki()
                elif answer == 4:
                    self.__exit_func()
                else:
                    print("Ошибка! Функции под таким номером нет!")
            except ValueError:
                print("Ошибка! Вы ввели некорректный символ!")

    def __edit_num_menu(self):
        checker = algorithmChecker()
        num_flag = True

        print("===Восстановление пропущенной цифры номера карты===\n"
              "-------------------------------------------------------------------")

        while num_flag:
            num = list(input(f"Введите номер карты(вместо пропущенной цифры введите x): "))
            if len(num) == 16 and self.__arr_for_check(num):
                num_flag = False

            missing_digit_index = num.index('x')

            for i in range(10):
                num[missing_digit_index] = str(i)

                if checker.first_algorithm(map(int, num)):
                    print(f'Пропущенное число: {i}')
                    num_flag = False
                
        self.start_menu()


    def __arr_for_check(self, num):
        arr = num.copy()
        if 'x' in arr:
            arr.remove('x')
        else:
            print("Ошибка! Вы не ввели 'x'!")
            return False
        if len(arr) == 15:
            try:
                for i in arr:
                    int(i)

            except ValueError:
                print("Ошибка! Введен некорректный символ")
                return False
        else:
            print("Ошибка! Введено более 1 пропущенной цифры!")
            return False
        return True

    def __check_menu(self):
        num = []
        answer = -1
        number_flag = True
        func_flag = True

        print(f"===Проверка номера карты на подлинность по алгоритму Луна===\n"
              f"---------------------------------------------------------------------------------\n")
        while number_flag:
            num = list(input(f"Введите номер карты: "))
            if len(num) == 16 and self.__arr_is_int(num):
                number_flag = False
            else:
                print("Введен некорректный номер карты!")

        while func_flag:
            try:
                answer = int(input(f"\n\n\n"
                               f"------------------------------\n"
                               f"==ABCD-EFGH-IJKL-MNOP==\n"
                               f"=={num[0]}{num[1]}{num[2]}{num[3]}-{num[4]}{num[5]}{num[6]}{num[7]}-{num[8]}{num[9]}{num[10]}{num[11]}-{num[12]}{num[13]}{num[14]}{num[15]}==\n"
                               f"-------------------------------\n"
                               f"Выберите функцию:\n"
                               f"1. Проверить подлинность\n"
                               f"2. Выход\n"))
            except ValueError:
                print("Введен неверный символ. Введите число!")

            if answer == 1:
                self.__check(num)
            elif answer == 2:
                self.start_menu()
            else:
                print("Ошибка! Функции под таким номером нет!")


    def __wiki(self):
        print("===================Расчет происходит по 2 вариациям алгоритма Луна:===================\n"
              "______________________________________________________________________________________\n"
              "______________________________________Алгоритм 1______________________________________\n"
              "1 шаг. Каждая цифра, находящаяся на нечетной позиции, умножается на 2\n"
              "       Если получившееся число больше 9, то из этого числа необходимо вычесть 9\n"
              "2 шаг. Складываются все образованные числа и к ним прибавляется числа, находящиеся\n"
              "       на четной позиции в нормере карты\n"
              "3 шаг. Если общая сумма кратна 10, то номер действителен,\n"
              "       если нет - то не действителен\n"
              "______________________________________________________________________________________\n"
              "______________________________________Алгоритм 2______________________________________\n"
              "1 шаг. Каждая цифра, находящаяся на нечетной позиции, умножается на 2\n"
              "2 шаг. Складываются все образованные числа и к ним прибавляется числа, находящиеся\n"
              "       на четной позиции в нормере карты\n"
              "3 шаг. К этому числу прибавляется количество цифр номера карты, которые больше 4\n"
              "4 шаг. Если общая сумма кратна 10, то номер действителен,\n"
              "       если нет - то не действителен\n"
              "______________________________________________________________________________________\n"
              "Если расчет по этим алгоритмам верный, то номер признается действительным\n\n"
              "=======================================================================================\n"
              "------------------------------Восстановление цифры-------------------------------------\n"
              "       Восттановение происходит путем подбора.\n"
              "1 шаг. Цифра '0' подставляется вместо пропуска.\n"
              "2 шаг. Алгоимом 1 проверяется дейстительость этого номера.\n"
              "3 шаг. Если номер действителен, то число является пропущенным\n"
              "4 шаг. Если нормер НЕдействителен, то берется следующее число и шаги 1-3 повторяются.\n"
              "       Это происходит до момента, когда не будет найденно пропущенное число.\n"
              "________________________________________________________________________________________\n"
              "Нажмите любую клавишу для продолжения..."
              )
        

    def __str_arr_to_int(self, arr):
        res = []

        try:
            for i in arr:
                res.append(int(i))
        except ValueError:
            print("Ошибка! Неверные данные!")
        return res

    def __check(self, arr):
        checker = algorithmChecker()
        if checker.check(self.__str_arr_to_int(arr)):
            print("Данный номер банковской карты является действительным по алгоритму Луна!")
            print("Нажмите любую клавишу для продолжения...")
            
        else:
            print("Ошибка! Данный номер банковской карты НЕ является действительным по алгоритму Луна!")
            print("Нажмите любую клавишу для продолжения...")
            

    def __exit_func(self):
        print("Завершение работы!")
        time.sleep(3)
        sys.exit()

    def __arr_is_int(self, arr):
        for i in arr:
            try:
                i = int(i)
            except ValueError:
                return False
        return True
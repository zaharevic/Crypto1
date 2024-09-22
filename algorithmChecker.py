from xmlrpc.client import boolean


class algorithmChecker:
    def first_algorithm(self, numbers):
        result = 0
        i = 0
        for number in numbers:
            if (i % 2) == 0:
                tmp = number * 2
                if tmp > 9:
                    tmp -= 9
                result += tmp
            else:
                result += number
            i += 1
        return not boolean((result % 10))


    def second_algorithm(self, numbers):
        result = 0
        big_num_counter = 0
        i = 0
        for number in numbers:
            if number > 4:
                big_num_counter += 1
            if (i % 2) == 0:
                result += number * 2
            else:
                result += number
            i += 1
        return not boolean((result % 10) + big_num_counter)


    def check(self, number):
        flag = True
        if self.first_algorithm(number):
            print("Номер является верным в соответствии с 1 алгоритмом")
        else:
            print("Ошибка! Номер НЕ является верным в соответствии с 1 алгоритмом")
            flag = False

        if self.second_algorithm(number):
            print("Номер является верным в соответствии со 2 алгоритмом")
        else:
            print("Ошибка! Номер НЕ является верным в соответствии со 2 алгоритмом")
            flag = False
        return flag
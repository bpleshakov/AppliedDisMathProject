# Класс вычисляет кнф и проверяет на выполнимость
class CnfComputer:

    def compute(self, root):
        conjunctions = []
        variables = root.get_vars()
        count = len(variables)
        if count > 31:
            raise Exception('Too many variables')
        iter_count = 2 ** count
        true_table = [False] * iter_count
        var_index = dict(zip(variables, range(count)))
        is_satisfiable = False
        for i in range(iter_count):
            curr_values = self.nToKBit(i, count)
            var_values = {}
            for key in var_index:
                var_values[key] = curr_values[var_index[key]]
            true_table[i] = root.set_and_evaluate(var_values)
            is_satisfiable = is_satisfiable or true_table[i]
            if not true_table[i]:
                operands = []
                for key in var_index:
                    value = curr_values[var_index[key]]
                    if not value:
                        operands.append(key)
                    else:
                        operands.append('~' + key)
                conjunctions.append('\\/'.join(operands))

        return ' /\\ '.join(conjunctions), is_satisfiable


    def nToKBit(self, n, K):
        output = [False] * K

        def loop(n, i):
            if n == 0:
                return output
            output[-i] = n & 1 == 1
            return loop(n >> 1, i + 1)

        return loop(n, 1)


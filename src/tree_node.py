# Класс-утилита, который представляет собой дерево выражений.
# С помощью обхода в глубину, позволяет делать следующие операции:
# 1. Получить список переменных.
# 2. Назначить каждой переменной значение и вычислить все дерево.

class TreeNode:
    value = None
    left = None
    right = None

    def set_and_evaluate(self, values):
        if self.is_leaf():
            return values.get(self.value)
        else:
            if self.value == '~':
                return not self.left.set_and_evaluate(values)
            elif self.value == '\\/':
                return self.left.set_and_evaluate(values) or self.right.set_and_evaluate(values)
            elif self.value == '/\\':
                return self.left.set_and_evaluate(values) and self.right.set_and_evaluate(values)
            elif self.value == '->':
                return not self.left.set_and_evaluate(values) or self.right.set_and_evaluate(values)
            elif self.value == '<->':
                return self.left.set_and_evaluate(values) == self.right.set_and_evaluate(values)
            else:
                raise Exception('Unknown boolean operation:', self.value)

    def get_vars(self):
        leafs = []
        if self.is_leaf():
            leafs.append(self.value)
        if self.left is not None:
            leafs.extend(self.left.get_vars())
        if self.right is not None:
            leafs.extend(self.right.get_vars())
        return sorted(list(set(leafs)))

    def is_leaf(self):
        return self.right is None and self.left is None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        res = 'Value: ' + self.value
        if self.left is not None:
            res += '\nleft child: {\n' + str(self.left) + '\n}'
        if self.right is not None:
            res += '\nright child: {\n' + str(self.right) + '\n}'
        lines = res.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append('\t' + line)
        return '\n'.join(new_lines)

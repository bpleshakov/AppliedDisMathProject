# Класс который конвертирует формулу в обратную польскую нотацию и строит дерево выражения.
class RpnConverter:
    # чем выше старшинство, тем раньше выполняется оператор.
    PRECEDENCE = {
        '~': 6,
        '/\\': 5,
        '\\/': 4,
        '->': 3,
        '<->': 2,
        '(': 1
    }

    def convert(self, tokens):
        operators_stack = []
        res = []
        for token in tokens:
            if token == '(':
                operators_stack.append(token)
            elif token in self.PRECEDENCE:
                if len(operators_stack) == 0:
                    operators_stack.append(token)
                else:
                    stack_top = operators_stack.pop()
                    stack_top_precedence = self.PRECEDENCE.get(stack_top)
                    token_precedence = self.PRECEDENCE.get(token)
                    if stack_top_precedence > token_precedence:
                        operators_stack.append(token)
                        res.append(stack_top)
                    else:
                        operators_stack.append(stack_top)
                        operators_stack.append(token)
            elif token == ')':
                stack_top = operators_stack.pop()
                while not stack_top == '(':
                    res.append(stack_top)
                    stack_top = operators_stack.pop()
            else:
                res.append(token)
        while not len(operators_stack) == 0:
            res.append(operators_stack.pop())
        return res

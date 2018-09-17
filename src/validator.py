# пуш-даун автомат для валидации формулы.
# По лемме о накачке нам не подходит конечный автомат, потому что формула должна иметь столько
# открывающих скобок, сколько закрывающих
class Validator:
    STACK = ['Z']
    OPERATORS = ['\\/', '/\\', '->', '<->']
    INVERSE = '~'
    OPEN_PARENTHESES = '('
    CLOSE_PARENTHESES = ')'

    def start(self, token):
        stack_top = self.STACK.pop()
        if token == self.INVERSE:
            return self.start, stack_top
        elif token == self.OPEN_PARENTHESES:
            return self.start, 'A' + stack_top
        elif token in self.OPERATORS or token == self.CLOSE_PARENTHESES:
            return self.bad, ''
        else:
            return self.var, stack_top

    def var(self, token):
        stack_top = self.STACK.pop()
        if token in self.OPERATORS:
            return self.start, stack_top
        elif token == self.CLOSE_PARENTHESES:
            if stack_top == 'A':
                return self.var, ''
            else:
                return self.bad, ''
        else:
            return self.bad, stack_top

    def bad(self, token):
        raise Exception('Bad state happened')

    def validate(self, tokens):
        current_state = self.start
        for token in tokens:
            current_state, to_stack = current_state(token)
            for c in to_stack[::-1]:
                self.STACK.append(c)
            if len(self.STACK) == 0:
                self.STACK.append('Z')
        stack_top = self.STACK.pop()
        if current_state != self.var:
            return False
        if stack_top == 'Z':
            return True
        else:
            return False

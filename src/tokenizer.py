# конечный автомат для токенизации исходной строки
class Tokenizer:
    DELIMITER = '|'

    def sym(self, char):
        if char.isalpha():
            return self.var, char
        elif char == '(' or char == ')' or char == '~':
            return self.sym, char + self.DELIMITER
        elif char == '<':
            return self.eq1, char
        elif char == '-':
            return self.imply, char
        elif char == '\\':
            return self.disj, char
        elif char == '/':
            return self.conj, char
        else:
            return self.bad, ''

    def var(self, char):
        if char.isalpha():
            return self.var, char
        elif char == '(' or char == ')' or char == '~':
            return self.sym, self.DELIMITER + char + self.DELIMITER
        elif char == '<':
            return self.eq1, self.DELIMITER + char
        elif char == '-':
            return self.imply, self.DELIMITER + char
        elif char == '\\':
            return self.disj, self.DELIMITER + char
        elif char == '/':
            return self.conj, self.DELIMITER + char
        else:
            return self.bad, self.DELIMITER + char

    def eq1(self, char):
        if char == '-':
            return self.eq2, char
        else:
            return self.bad, ''

    def eq2(self, char):
        if char == '>':
            return self.sym, char + self.DELIMITER
        else:
            return self.bad, ''

    def imply(self, char):
        if char == '>':
            return self.sym, char + self.DELIMITER
        else:
            return self.bad, ''

    def conj(self, char):
        if char == '\\':
            return self.sym, char + self.DELIMITER
        else:
            return self.bad, ''

    def disj(self, char):
        if char == '/':
            return self.sym, char + self.DELIMITER
        else:
            return self.bad, ''

    def bad(self, char):
        raise Exception('Bad state happened')

    def tokenize(self, equation):
        tokens = ''
        current_state = self.sym
        for c in equation:
            if c.isspace():
                continue
            current_state, write = current_state(c)
            tokens += write

        tokens = tokens.split(self.DELIMITER)
        return [x for x in tokens if len(x) > 0]

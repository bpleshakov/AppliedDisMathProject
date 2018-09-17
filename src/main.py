from tokenizer import Tokenizer
from validator import Validator
from rpn_converter import RpnConverter
from expression_tree_converter import ExpressionTreeConverter
from cnf_computer import CnfComputer

def main():
    tokenizer = Tokenizer()
    validator = Validator()
    rpn_converter = RpnConverter()
    expression_tree_converter = ExpressionTreeConverter()
    cnf_computer = CnfComputer()
    equation = input()
    print('Initial formula:', equation)
    tokens = tokenizer.tokenize(equation)
    print('Tokens:', tokens)
    is_valid = validator.validate(tokens)
    print('Is a valid formula? ', is_valid)

    if is_valid:
        rpn = rpn_converter.convert(tokens)
        print('Reversed Polish Notation', rpn)
        root = expression_tree_converter.convert(rpn)
        print('Expression Tree: \n', root)
        cnf, is_satisfiable = cnf_computer.compute(root)
        print('CNF: ', cnf)
        print('Is satisfiable? ', is_satisfiable)


if __name__ == '__main__':
    main()

from tree_node import TreeNode


class ExpressionTreeConverter:

    OPERANDS = {
        '~': 1,
        '/\\': 2,
        '\\/': 2,
        '->': 2,
        '<->': 2
    }

    def convert(self, tokens):
        stack = []
        for token in tokens:
            if token in self.OPERANDS:
                operands_count = self.OPERANDS.get(token)
                node = TreeNode(token)
                if operands_count == 1:
                    node.left = stack.pop()
                else:
                    node.right = stack.pop()
                    node.left = stack.pop()
                stack.append(node)
            else:
                stack.append(TreeNode(token))
        return node

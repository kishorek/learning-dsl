import parsimonious
from parsimonious.nodes import NodeVisitor

calculator_grammar = parsimonious.Grammar(
    """
    expression = number ws arith_op ws number
    number = ~r"\d+"
    arith_op = add_op / sub_op
    sub_op = "-"
    add_op = "+"
    ws = ~r"\s*"
    """
)


class CalculatorVisitor(NodeVisitor):
    def visit_number(self, node, visited_children):
        return int(node.text)

    # def visit_arith_op(self, node, visited_children):
    #     return node.text

    # def visit_add_op(self, node, visited_children):
    #     return node.text

    # def visit_sub_op(self, node, visited_children):
    #     return node.text

    def generic_visit(self, node, visited_children):
        """The generic visit method."""
        return node.text

    def visit_expression(self, node, visited_children):
        left, _, op_node, _, right = visited_children

        if op_node == "+":
            return left + right
        elif op_node == "-":
            return left - right

    def visit_ws(self, node, visited_children):
        pass


def parse_calculator(expr):
    tree = calculator_grammar.parse(expr)
    visitor = CalculatorVisitor()
    return visitor.visit(tree)


# Test the parser
expression1 = "1 + 2"
expression2 = "1 - 2"
print(parse_calculator(expression1))  # Output: 3
print(parse_calculator(expression2))  # Output: -1

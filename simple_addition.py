import parsimonious
from parsimonious.nodes import NodeVisitor

calculator_grammar = parsimonious.Grammar(
    """
    expression = number ws add_op ws number
    number = ~r"\d+"
    add_op = "+"
    ws = ~r"\s*"
"""
)


class CalculatorVisitor(NodeVisitor):
    def visit_number(self, node, visited_children):
        return int(node.text)

    def visit_add_op(self, node, visited_children):
        return node.text

    def visit_expression(self, node, visited_children):
        left, _, _, _, right = visited_children
        return left + right

    def visit_ws(self, node, visited_children):
        pass


def parse_calculator(expr):
    tree = calculator_grammar.parse(expr)
    visitor = CalculatorVisitor()
    return visitor.visit(tree)


# Test the parser
expression = "1+ 2"
print(parse_calculator(expression))  # Output: 3

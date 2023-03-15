import parsimonious
from parsimonious.nodes import NodeVisitor

calculator_grammar = parsimonious.Grammar(
    """
    expression = first_exp ws arith_op ws number
    first_exp =  number ws arith_op ws number
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

    def visit_add_op(self, node, visited_children):
        return node.text

    def visit_first_exp(self, node, visited_children):
        left, _, op, _, right = visited_children
        if op == "+":
            return left + right
        elif op == "-":
            return left - right

    def visit_expression(self, node, visited_children):
        left, _, op, _, right = visited_children
        if op == "+":
            return left + right
        elif op == "-":
            return left - right

    def generic_visit(self, node, visited_children):
        return node.text

    def visit_ws(self, node, visited_children):
        pass


def parse_calculator(expr):
    tree = calculator_grammar.parse(expr)
    visitor = CalculatorVisitor()
    return visitor.visit(tree)


# Test the parser
expression = "4 + 2 - 4"
print(parse_calculator(expression))  # Output: 2

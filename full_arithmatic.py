import parsimonious
from parsimonious.nodes import NodeVisitor

grammar = parsimonious.Grammar(
    """
    expression = term (add_op term)*
    term = factor (mul_op factor)*
    factor = number / parenth_expr
    parenth_expr = "(" expression ")"
    add_op = "+" / "-"
    mul_op = "*" / "/"
    number = ~r"\d+(\.\d+)?"
"""
)


class ArithmeticVisitor(NodeVisitor):
    def visit_number(self, node, visited_children):
        return float(node.text)

    def visit_add_op(self, node, visited_children):
        return node.text

    def visit_mul_op(self, node, visited_children):
        return node.text

    def visit_parenth_expr(self, node, visited_children):
        return visited_children[1]

    def visit_expression(self, node, visited_children):
        result = visited_children[0]

        for op, term in visited_children[1]:
            if op == "+":
                result += term
            elif op == "-":
                result -= term

        return result

    def visit_term(self, node, visited_children):
        result = visited_children[0]

        for op, factor in visited_children[1]:
            if op == "*":
                result *= factor
            elif op == "/":
                result /= factor

        return result


def parse_arithmetic(expr):
    tree = grammar.parse(expr)
    visitor = ArithmeticVisitor()
    return visitor.visit(tree)


# Test the parser
print(parse_arithmetic("2 + 3 * (4 - 1)"))

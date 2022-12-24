from icecream import ic

from parsimonious.grammar import Grammar,NodeVisitor

ic.configureOutput(includeContext=True)

div_grammar = Grammar(r"""
addition = number "+" number
number = ~"[0-9]+"
""")

class AdditionVisitor(NodeVisitor):
    # def visit_expr(self, node, visited_children):
    #     ic(visited_children)
    #     return int(visited_children[0])-int(visited_children[-1])

    def visit_addition(self, node, visited_children):
        ic(visited_children)
        return int(visited_children[0])+int(visited_children[-1])

    def visit_number(self, node, visited_children):
        ic(visited_children)
        ic(node)
        return node.text

    # For the nodes that are not specified in the Visitor
    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node


tree = div_grammar.parse("1+2")
# print(tree)

dv = AdditionVisitor()
output = dv.visit(tree)
from pprint import pprint
pprint(output)

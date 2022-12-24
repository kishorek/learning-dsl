from icecream import ic

from parsimonious.grammar import Grammar,NodeVisitor

ic.configureOutput(includeContext=True)

class WordVisitor(NodeVisitor):

    def visit_word(self, node, visited_children):
        ic(node)
        """ Makes a dict of the section (as key) and the key/value pairs. """
        #return node.text # with the comma
        return node.text
    

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node

grammar = Grammar(
    r"""
        word        = ~r"\w+"
        ws          = ~"\s*"
        emptyline   = ws+
    """)

data = """hello"""

tree = grammar.parse(data)

cv = WordVisitor()
output = cv.visit(tree)
ic(output)

import parsimonious
from parsimonious.nodes import NodeVisitor

emoticon_grammar = parsimonious.Grammar(
    """
    emoticon = smiley / frowny
    smiley = ":-)"
    frowny = ":-("
    """
)


class EmoticonVisitor(NodeVisitor):
    def visit_smiley(self, node, visited_children):
        return "smiley"

    def visit_frowny(self, node, visited_children):
        return "frowny"

    def visit_emoticon(self, node, visited_children):
        return visited_children[0]


def parse_emoticon(emoticon_str):
    tree = emoticon_grammar.parse(emoticon_str)
    visitor = EmoticonVisitor()
    return visitor.visit(tree)


# Test the parser
emoticon1 = ":-)"
emoticon2 = ":-("
print(parse_emoticon(emoticon1))  # Output: smiley
print(parse_emoticon(emoticon2))  # Output: frowny

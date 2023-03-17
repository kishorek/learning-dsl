from parsimonious.grammar import Grammar, NodeVisitor

grammar = Grammar(
    r"""
        h1_line     = h1 line
        line        = ws (word ws)* (emptyline)*
        h1          = ~r"^#"
        word        = ~r"\w+"
        ws          = ~"\s*"
        emptyline   = ws+
    """
)


class MarkdownVisitor(NodeVisitor):
    def visit_h1_line(self, node, visited_children):
        tag, text = visited_children
        return tag.replace("###", text)

    def visit_line(self, node, visited_children):
        return node.text.strip()

    def visit_h1(self, node, visited_children):
        return "<h1>###</h1>"

    def generic_visit(self, node, visited_children):
        """The generic visit method."""
        return visited_children or node


def parse_markdown(expr):
    tree = grammar.parse(expr)
    visitor = MarkdownVisitor()
    return visitor.visit(tree)


# Test the parser
content = "# This is a header 1"
print(parse_markdown(content))

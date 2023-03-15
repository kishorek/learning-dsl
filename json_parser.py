import json
import parsimonious
from parsimonious.nodes import NodeVisitor

json_grammar = parsimonious.Grammar(
    """
    value = ws (object / array / string / number / "true" / "false" / "null") ws
    object = "{" (ws key_value (ws "," ws key_value)* ws)? "}"
    key_value = string ws ":" ws value
    array = "[" (ws value (ws "," ws value)* ws)? "]"
    string = "\"" ~r"[^\"\\\\]*" "\""
    number = "-"? ("0" / ([1-9] digits?)) ("." digits)? exp?
    digits = ~r"\d+"
    exp = ("e" / "E") ("+" / "-")? digits
    ws = ~r"\s*"
"""
)


class JSONVisitor(NodeVisitor):
    def visit_value(self, node, visited_children):
        _, value, _ = visited_children
        return value[0]

    def visit_object(self, node, visited_children):
        _, key_values, _ = visited_children
        return dict(key_values[0] or [])

    def visit_key_value(self, node, visited_children):
        key, _, _, _, value = visited_children
        return key, value

    def visit_array(self, node, visited_children):
        _, values, _ = visited_children
        return values[0] or []

    def visit_string(self, node, visited_children):
        return node.text[1:-1]

    def visit_number(self, node, visited_children):
        return float(node.text)

    def visit_ws(self, node, visited_children):
        pass


def parse_json(json_str):
    tree = json_grammar.parse(json_str)
    visitor = JSONVisitor()
    return visitor.visit(tree)


# Test the parser
json_str = '{"key": "value", "numbers": [1, 2, 3], "nested": {"a": 1, "b": true}}'
print(parse_json(json_str))

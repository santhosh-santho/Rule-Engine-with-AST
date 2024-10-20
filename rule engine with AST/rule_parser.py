import ast

def parse_rule(rule_string):
    try:
        parsed_ast = ast.parse(rule_string, mode='eval')
        return convert_ast(parsed_ast.body)
    except SyntaxError as e:
        raise ValueError(f"Invalid rule string: {e}")

def convert_ast(node):
    if isinstance(node, ast.BinOp):
        return Node(node.op.__class__.__name__, left=convert_ast(node.left), right=convert_ast(node.right))
    elif isinstance(node, ast.Compare):
        return Node(node.ops[0].__class__.__name__, left=convert_ast(node.left), right=convert_ast(node.comparators[0]))
    elif isinstance(node, ast.Name):
        return Node("operand", value=node.id)
    elif isinstance(node, ast.Constant):
        return Node("operand", value=node.value)
    else:
        raise ValueError("Unsupported node type")
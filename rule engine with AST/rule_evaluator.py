def evaluate_rule(ast, data):
    if ast.type == "And":
        return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
    elif ast.type == "Or":
        return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    elif ast.type == "Eq":
        return data.get(ast.left.value) == ast.right.value
    elif ast.type == "Gt":
        return data.get(ast.left.value) > ast.right.value
    elif ast.type == "Lt":
        return data.get(ast.left.value) < ast.right.value
    else:
        raise ValueError("Unsupported operator")
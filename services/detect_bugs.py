import ast

issues = []


def check_syntax(path):
    """ Check Code for Code Analysis, Code Transformation, tooling and Automation """
    
    try:
        with open(path, "r") as file:
            content = file.read()

        tree = ast.parse(content)
        issues.clear()

        visitor = FunctionCallVisitor()
        visitor.visit(tree)

        for node in ast.walk(tree):
            if isinstance(node, ast.Try) and not node.handlers:
                issues.append("Empty except block found")
            elif isinstance(node, ast.ExceptHandler) and isinstance(node.type, ast.Name) and node.type.id == 'Exception':
                issues.append("Empty except clause found")

        if issues:
            return f"Potential bugs are found for {path}: " + "\n".join(issues)
        else:
            return f"No bugs are found for {path}"

    except Exception as e:
        return f"Failed to analyze file {path}, Errors: {str(e)}"


class FunctionCallVisitor(ast.NodeVisitor):
    """ Static Analysis """
    def visit_Call(self, node):

        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            args = [arg for arg in node.args if isinstance(arg, ast.Str)]
            if args:
                print("Detected print statements with string literals")
                for arg in args:
                    print(arg.s)
                    issues.append(arg.s)

        # return super().visit_Call(node)
        return self.generic_visit(node)
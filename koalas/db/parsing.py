import sqlparse as sp

def parse_statements(stmts):
    return [parse_statement(stmt) for stmt in stmts]

def parse_statement(statement):
    stmt = sp.parse(statement)[0]
    tokens = [t for t in stmt.tokens if not token.is_whitespace()
            and token._get_repr_name() != 'Comment']
    functions = {}

    for token in tokens:
        pass
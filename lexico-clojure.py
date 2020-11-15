import ply.lex as lex

# Reserved words
reserved = {'def': 'DEF', 'defn': 'DEFN', 'nil': 'NULL', 'true': 'BOOLEAN', 'false': 'BOOLEAN',
            'and': 'AND', 'or': 'OR', 'not': 'NOT', 'if': 'IF', 'else': 'ELSE', 'println': 'Function',
            'set': 'SET', 'union': 'UNION', 'difference': 'DIFFERENCE', 'intersection': 'INTERSECTION',
            }

# List of token names.
tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
'LCURLYBRA',
'RCURLYBRA',
'SETDEF',
'ID',
'FLOAT',
'EQUAL',
'NOTEQUAL',
) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCURLYBRA = r'\{'
t_RCURLYBRA = r'\}'
t_SETDEF = r'\#'
t_NUMBER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_EQUAL =  r'='
t_NOTEQUAL =  r'not='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

linea = input("-> ")
    
while linea!= "":
    lexer.input(linea)    
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    linea = input("-> ")
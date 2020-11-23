import ply.lex as lex

# Reserved words
reserved = {'def': 'DEF', 'defn': 'DEFN', 'nil': 'NULL', 'true': 'BOOLEAN_TRUE', 'false': 'BOOLEAN_FALSE',
            'and': 'AND', 'or': 'OR', 'not': 'NOT', 'if': 'IF', 'else': 'ELSE', 'println': 'FUNCTION_PRINTLN',
            'set': 'SET', 'union': 'UNION', 'difference': 'DIFFERENCE', 'intersection': 'INTERSECTION',
            'while':'WHILE', 'do':'DO', 'doseq':'FOR', 'read':'READ','line':'LINE', 'empty':'FUNCTION_EMPTY',
            'str':'TYPE_STR', 'subs':'FUNCTION_SUB', 'seq':'FUNCTION_SEQ', 'get':'FUNCTION_GET', 'count':'FUNCTION_COUNT',
            'conj':'FUNCTION_CONJ', 'vector': 'VECTOR', 'list': 'LIST', 'nth': 'FUNCTION_NTH'}

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
'STRING',
'GREATERTHAN',
'LESSTHAN',
'GREATERTHANEQUALS',
'LESSTHANEQUALS',
'APOSTROPHE',
'LBRACKET',
'RBRACKET',
'QUESTION',
'DOUBLE_POINT',
'POINT',
'PERCENTAJE',
'AT',
'EXCLAMATION'
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
#t_NUMBER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_EQUAL =  r'='
t_NOTEQUAL =  r'not='
t_GREATERTHAN = r'\>'
t_LESSTHAN= r'\<'
t_GREATERTHANEQUALS  = r'\>\='
t_LESSTHANEQUALS  = r'\<\='
t_APOSTROPHE = r'\''
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_QUESTION  = r'\?'
t_DOUBLE_POINT  = r'\:'
t_POINT  = r'\.'
t_PERCENTAJE  = r'\%'
t_AT  = r'\@'
t_EXCLAMATION  = r'\!'


#Esta ER fue añadidad para poder obtener el resultado de las operaciones
#entre enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.type=reserved.get(t.value, 'STRING')
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


"""
linea = input("-> ")
    
while linea!= "":
    lexer.input(linea)    
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    linea = input("-> ")


#Funcion para oder analizar un solo string 
def analizar(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
        
archivo = open("codigo.txt")
for linea in archivo:
    if linea[0]!='#':
        print(">> "+linea)
        analizar(linea)
        if len(linea)==0:
            break

"""

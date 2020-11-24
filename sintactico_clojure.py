import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from lexico_clojure import tokens

def p_stament(p):
     '''stament : LPAREN compute RPAREN
                | vector'''
     if p[1] == '(' and p[3] == ')':
          p[0] = p[2]

def p_compute(p):
     '''compute : expression
                | function'''
     p[0] = p[1]

### Funciones escritas por Marck Murillo
def p_function_println(p):
     'function : FUNCTION_PRINTLN STRING'
     p[0] = 'nil'

def p_function_readLine(p):
     'function : READ MINUS LINE'

def p_function_empty(p):
     'function : FUNCTION_EMPTY QUESTION STRING'

def p_multiplestring(p):
     '''multiplestring : STRING
                        | multiplestring STRING'''
                         
def p_function_concant(p):
     'function : TYPE_STR multiplestring'

def p_function_subString(p):
     'function : FUNCTION_SUB STRING NUMBER'

def p_function_sequence(p):
     'function : FUNCTION_SEQ STRING'

     
def p_multipleObjects(p):
     '''multipleObjects : STRING
                        | NUMBER
                        | FLOAT
                        | BOOLEAN_TRUE
                        | BOOLEAN_FALSE
                        | multipleObjects STRING
                        | multipleObjects NUMBER
                        | multipleObjects FLOAT
                        | multipleObjects BOOLEAN_TRUE
                        | multipleObjects BOOLEAN_FALSE'''

def p_vector(p):
     'vector : LBRACKET multipleObjects RBRACKET'


def p_function_get(p):
     'function : FUNCTION_GET sequential_colls NUMBER'

def p_function_count(p):
     'function : FUNCTION_COUNT sequential_colls'

def p_function_conj(p):
     'function : FUNCTION_CONJ sequential_colls multipleObjects'

#Modifiqué estas cosas Marck. :3

### Fin funciones escritas por Marck Murillo

### Inicio funciones escritas por Franklin Ordóñez
def p_list(p):
    '''list : APOSTROPHE LPAREN multipleObjects RPAREN
        | LPAREN LIST multipleObjects RPAREN'''

def p_sequential_colls(p):
    'sequential_colls : vector | set | list | ID'

def p_set(p):
    '''set : SETDEF LCURLYBRA multipleObjects RCURLYBRA
        | LPAREN SET multipleObjects RPAREN'''

def p_setFunctions_union(p):
    'setFunctions_union : SET DIVIDE UNION set set'

def p_setFunctions_difference(p):
    'setFunctions_difference : SET DIVIDE DIFFERENCE set set'

def p_setFunctions_intersection(p):
    'setFunctions_intersection : SET DIVIDE INTERSECTION set set'

def p_function_take(p):
    'function_take : LPAREN TAKE NUMBER sequential_colls'

def p_function_drop(p):
    'function_drop : LPAREN DROP NUMBER sequential_colls'


### Fin funciones escritas por Franklin Ordóñez
def p_expression_plus(p):
     'expression : expression PLUS term'
     p[0] = p[1] + p[3]
 
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('clojure > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)







   

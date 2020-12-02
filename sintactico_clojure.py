import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from lexico_clojure import tokens

def p_stament(p):
     'stament : LPAREN compute RPAREN'
     p[0] = p[2]

def p_compute(p):
     '''compute : function
                | general_expression
                | control_structure code_block
                | while'''
     p[0] = p[1]

def p_code_block(p):
     '''code_block : LPAREN function RPAREN
                   | LPAREN general_expression RPAREN
                   | LPAREN function RPAREN code_block 
                   | LPAREN general_expression RPAREN code_block '''

### Funciones escritas por Marck Murillo
def p_function_println(p):
     'function : FUNCTION_PRINTLN multipleObjects'
     p[0] = 'FUNCTION_PRINTLN'

def p_function_readLine(p):
     'function : READLINE'
     p[0] = input(">> ")

def p_function_empty(p):
     'function : FUNCTION_EMPTY STRING'
     p[0] = 'FUNCTION_EMPTY'

def p_multiplestring(p):
    '''multiplestring : STRING
                      | STRING multiplestring
                      | stament
                      | stament multiplestring'''
    p[0] = p[1]

                         
def p_function_str(p):
     'function : TYPE_STR multiplestring'
     p[0] = "CONCATENATION_STR"

def p_function_subString(p):
     '''function : FUNCTION_SUB STRING NUMBER
                 | FUNCTION_SUB ID NUMBER'''
     p[0] = 'FUNCTION_SUBSTRING'

def p_function_sequence(p):
     '''function : FUNCTION_SEQ STRING
                 | FUNCTION_SEQ ID'''
     p[0] = 'FUNCTION_SEQ'

     
def p_multipleObjects(p):
     '''multipleObjects : value
                        | value multipleObjects
                        | sequential_colls
                        | sequential_colls multipleObjects'''
     p[0] = p[1]
     
def p_value(p):
     '''value : STRING
              | NUMBER
              | FLOAT
              | BOOLEAN_TRUE
              | BOOLEAN_FALSE'''
     p[0] = p[1]

def p_vector(p):
     '''vector : LBRACKET multipleObjects RBRACKET
               | LPAREN VECTOR multipleObjects RPAREN'''
     p[0] = 'VECTOR'


def p_function_get(p):
     'function : FUNCTION_GET sequential_colls NUMBER'
     p[0] = 'FUNCTION GET'

def p_function_count(p):
     'function : FUNCTION_COUNT sequential_colls'
     p[0] = 'FUNCTION COUNT'

def p_function_conj(p):
     'function : FUNCTION_CONJ sequential_colls multipleObjects'
     p[0] = 'FUNCTION CONJ'


#Modifiqué estas cosas Marck. :3

### Fin funciones escritas por Marck Murillo

### Inicio funciones escritas por Franklin Ordóñez
def p_list(p):
     '''list : APOSTROPHE LPAREN multipleObjects RPAREN
        | LPAREN LIST multipleObjects RPAREN'''
     p[0] = 'LIST'

def p_sequential_colls(p):
     '''sequential_colls : vector
                        | set
                        | list
                        | ID'''
     p[0] = p[1]

def p_set(p):
     '''set : SETDEF LCURLYBRA multipleObjects RCURLYBRA
             | LPAREN SET multipleObjects RPAREN'''
     p[0] = 'SET'

def p_setFunctions_union(p):
    'setFunctions_union : SET DIVIDE UNION set set'
    p[0] = 'SET UNION'

def p_setFunctions_difference(p):
    'setFunctions_difference : SET DIVIDE DIFFERENCE set set'
    p[0] = 'SET DIFFERENCE'

def p_setFunctions_intersection(p):
    'setFunctions_intersection : SET DIVIDE INTERSECTION set set'
    p[0] = 'SET INTERSECTION'

def p_function_take(p):
    'function_take : TAKE NUMBER sequential_colls'
    p[0] = 'FUNCTION TAKE'

def p_function_drop(p):
    'function_drop : DROP NUMBER sequential_colls'
    p[0] = 'FUNCTION DROP'


### Fin funciones escritas por Franklin Ordóñez

#Funciones escritas por George Henriquez
###Operaciones aritmeticas - George Henriquez
def p_general_expression(p):
    '''general_expression : math_operation
                          | boolean_operation
                          | variable_expression
                          | setFunctions_union
                          | setFunctions_intersection
                          | setFunctions_difference
                          | function_take
                          | function_drop'''
    p[0] = p[1]

def p_num_expression(p):
    '''num_expression : LPAREN math_operation RPAREN'''
    p[0] = p[2]

def p_operation_plus(p):
    '''math_operation : PLUS num_expression num_expression'''
    p[0] = 'Addition'

def p_operation_minus(p):
    '''math_operation : MINUS num_expression num_expression'''
    p[0] = 'Subtraction'

def p_operation_divide(p):
    '''math_operation : DIVIDE num_expression num_expression'''
    p[0] = 'Division'

def p_operation_times(p):
    '''math_operation : TIMES num_expression num_expression'''
    p[0] = 'Multiplication'

def p_number(p): 
    '''num_expression : NUMBER
                      | ID'''
    p[0] = p[1]

###Operaciones Booleanas - George Henriquez
def p_boolean_operation(p):
     '''boolean_operation : bool_operation
                          | compare_operation'''
     p[0] = p[1]

def p_boolean_expression(p):
     'bool_expression : LPAREN bool_operation RPAREN'
     p[0] = p[2]

def p_bool_operation_and(p):
     '''bool_operation : AND bool_expression bool_expression'''
     p[0] = 'AND Operation'

def p_bool_operation_or(p):
     '''bool_operation : OR bool_expression bool_expression'''
     p[0] = 'OR Operation'

def p_bool_operation_not(p):
     '''bool_operation : NOT bool_expression'''
     p[0] = 'NOT Operation'

def p_bool_type(p):
     '''bool_expression : BOOLEAN_TRUE
     | BOOLEAN_FALSE
     | ID'''
     p[0] = p[1]

###Operaciones de Comparacion - George Henriquez
def p_compare_operation_greaterthan(p):
     'compare_operation : GREATERTHAN num_expression num_expression'
     p[0] = 'GREATERTHAN Operation'

def p_compare_operation_lessthan(p):
     'compare_operation : LESSTHAN num_expression num_expression'
     p[0] = 'LESSTHAN Operation'

def p_compare_operation_greaterthan_equals(p):
     'compare_operation : GREATERTHANEQUALS num_expression num_expression'
     p[0] = 'GREATER THAN EQUALS Operation'

def p_compare_operation_lessthan_equals(p):
     'compare_operation : LESSTHANEQUALS num_expression num_expression'
     p[0] = 'LESS THAN EQUALS Operation'

def p_compare_operation_equal(p):
     'compare_operation : EQUAL num_expression num_expression'
     p[0] = 'EQUAL Operation'

def p_compare_operation_notequal(p):
     'compare_operation : NOTEQUAL num_expression num_expression'
     p[0] = 'NOT EQUAL Operation'

#Definicion de variables
def p_variable_expression_statemt(p):
     '''variable_expression : DEF ID value
                            | DEF ID sequential_colls
                            | DEF ID stament''' 
     p[0] = f'{p[2]} = {p[3]}' 


#Estructuras de control
def p_control_structure(p):
     '''control_structure : if
                          | for'''
     p[0] = p[1]

def p_for(p):
    '''for : FOR LBRACKET ID sequential_colls RBRACKET
           | FOR LBRACKET ID ID RBRACKET'''
    p[0] = 'for'

def p_while(p):
     '''while : WHILE LPAREN boolean_operation RPAREN do'''
     p[0] = 'while'

def p_do_statement(p):
     'do : LPAREN DO code_block RPAREN'
     p[0] = 'do'

def p_if(p):
    '''if : IF LPAREN boolean_operation RPAREN '''
    p[0] = 'if'



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


#funciones de error

"""
def p_error(token):
    if token is not None:
        print ("El token '%s' no es valido ( linea %s )" % (token.value, token.lineno))
    else:
        print('ingreso no valido')
"""


#funcion de error para la interfaz        
def p_error(token):
     log = open("log.txt", "w")
     if token is not None:
          print ("El token '%s' no es valido ( linea %s )" % (token.value, token.lineno), file = log)
     else:
          print('ingreso no valido', file = log)



# Build the parser
parser = yacc.yacc()


# #Funcion para probar -Henriquez
# def prueba():
#     print("Prueba Operaciones")
#     linea = "(+ (* (- 8 4) 2) 2)"
#     print("clojure > " + linea)
#     result = parser.parse(linea)
#     print(result)
#     linea = "(> 9 2)"
#     print("clojure > " + linea)
#     result = parser.parse(linea)
#     print(result)
#     linea = "(def variable true)"
#     print("clojure > " + linea)
#     result = parser.parse(linea)
#     print(result)
#     linea = "(and true false)"
#     print("clojure > " + linea)
#     result = parser.parse(linea)
#     print(result)

# #Funcion para probar -Marck Murillo
# def prueba1():
#      print("Prueba Murillo")
#      linea = "(println \"Ingrese su nombre: \")"
#      print("clojure > " + linea)
#      result = parser.parse(linea)
#      print(result)
#      linea = "(def nombre (read-line))"
#      print("clojure > " + linea)
#      result = parser.parse(linea)
#      print(result)
#      linea = "(println \"Ingrese su edad: \")"
#      print("clojure > " + linea)
#      result = parser.parse(linea)
#      print(result)
#      linea = "(def edad (read-line))"
#      print("clojure > " + linea)
#      result = parser.parse(linea)
#      print(result)
#      linea = "(def nombresecreto (str (subs nombre 2) edad) )"
#      print("clojure > " + linea)
#      result = parser.parse(linea)
#      print(result)
#      linea = "(println \"tu Nombre secreto es: \" nombresecreto)"
#      print("clojure > " + linea)
#      result = parser.parse(linea)
#      print(result)
#      linea = "(println \"el cual se deletrea: \" (seq nombresecreto))"
#      print("clojure > " + linea)
#      result = parser.parse(linea)
#      print(result)

     



# #Función para probar -Ordóñez
# def prueba_2():
#     print("Prueba creación de lista")
#     linea = "(list 1 2 3)"
#     print("clojure > "+linea)
#     result = parser.parse(linea)
#     print(result)
#     print("Prueba unión dos sets")
#     linea = "(set/union #{1 2 3} #{1 2 4})"
#     print("clojure > " + linea)
#     print(result)
#     result = parser.parse(linea)
#     print(result)
#     print("Prueba de funcion take")
#     linea = "(take 1 [1 2 3])"
#     print("clojure > " + linea)
#     result = parser.parse(linea)
#     print(result)
#     print("Prueba de funcion drop")
#     linea = "(drop 1 [1 2 3])"
#     print("clojure > " + linea)
#     result = parser.parse(linea)
#     print(result)
#     print("Prueba de diferencia dos sets")
#     linea = "(set/difference #{1 2 3} #{1 2 4})"
#     print("clojure > " + linea)
#     result = parser.parse(linea)
#     print(result)

# prueba_2()

# prueba()
# prueba1()

"""
while True:
   try:
       s = input('clojure > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

"""


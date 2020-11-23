
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER PLUS MINUS TIMES DIVIDE LPAREN RPAREN LCURLYBRA RCURLYBRA SETDEF ID FLOAT EQUAL NOTEQUAL STRING GREATERTHAN LESSTHAN GREATERTHANEQUALS LESSTHANEQUALS APOSTROPHE LBRACKET RBRACKET QUESTION DOUBLE_POINT POINT PERCENTAJE AT EXCLAMATION DEF DEFN NULL BOOLEAN_TRUE BOOLEAN_FALSE AND OR NOT IF ELSE FUNCTION_PRINTLN SET UNION DIFFERENCE INTERSECTION WHILE DO FOR READ LINE FUNCTION_EMPTY TYPE_STR FUNCTION_SUB FUNCTION_SEQ FUNCTION_GET FUNCTION_COUNT FUNCTION_CONJ VECTOR LIST FUNCTION_NTHstament : LPAREN compute RPAREN\n                | vectorcompute : expression\n                | functionfunction : FUNCTION_PRINTLN STRINGfunction : READ MINUS LINEfunction : FUNCTION_EMPTY QUESTION STRINGmultiplestring : STRING\n                        | multiplestring STRINGfunction : TYPE_STR multiplestringfunction : FUNCTION_SUB STRING NUMBERfunction : FUNCTION_SEQ STRINGmultipleObjects : STRING\n                        | NUMBER\n                        | FLOAT\n                        | BOOLEAN_TRUE\n                        | BOOLEAN_FALSE\n                        | multipleObjects STRING\n                        | multipleObjects NUMBER\n                        | multipleObjects FLOAT\n                        | multipleObjects BOOLEAN_TRUE\n                        | multipleObjects BOOLEAN_FALSEvector : LBRACKET multipleObjects RBRACKETfunction : FUNCTION_GET vector NUMBERfunction : FUNCTION_COUNT vectorfunction : FUNCTION_CONJ vector multipleObjectsexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'LPAREN':([0,2,5,29,30,31,32,],[2,5,5,5,5,5,5,]),'LBRACKET':([0,17,18,19,],[4,4,4,4,]),'$end':([1,3,28,43,],[0,-2,-1,-23,]),'FUNCTION_PRINTLN':([2,],[10,]),'READ':([2,],[11,]),'FUNCTION_EMPTY':([2,],[12,]),'TYPE_STR':([2,],[13,]),'FUNCTION_SUB':([2,],[14,]),'FUNCTION_SEQ':([2,],[16,]),'FUNCTION_GET':([2,],[17,]),'FUNCTION_COUNT':([2,],[18,]),'FUNCTION_CONJ':([2,],[19,]),'NUMBER':([2,4,5,21,22,23,24,25,26,29,30,31,32,38,40,42,43,44,45,46,47,48,59,],[15,23,15,45,-13,-14,-15,-16,-17,15,15,15,15,57,58,23,-23,-18,-19,-20,-21,-22,45,]),'STRING':([4,10,13,14,16,21,22,23,24,25,26,35,36,37,42,43,44,45,46,47,48,56,59,],[22,33,37,38,39,44,-13,-14,-15,-16,-17,55,56,-8,22,-23,-18,-19,-20,-21,-22,-9,44,]),'FLOAT':([4,21,22,23,24,25,26,42,43,44,45,46,47,48,59,],[24,46,-13,-14,-15,-16,-17,24,-23,-18,-19,-20,-21,-22,46,]),'BOOLEAN_TRUE':([4,21,22,23,24,25,26,42,43,44,45,46,47,48,59,],[25,47,-13,-14,-15,-16,-17,25,-23,-18,-19,-20,-21,-22,47,]),'BOOLEAN_FALSE':([4,21,22,23,24,25,26,42,43,44,45,46,47,48,59,],[26,48,-13,-14,-15,-16,-17,26,-23,-18,-19,-20,-21,-22,48,]),'RPAREN':([6,7,8,9,15,20,22,23,24,25,26,27,33,36,37,39,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,],[28,-3,-4,-29,-33,-32,-13,-14,-15,-16,-17,49,-5,-10,-8,-12,-25,-23,-18,-19,-20,-21,-22,-34,-27,-28,-30,-31,-6,-7,-9,-11,-24,-26,]),'PLUS':([7,9,15,20,27,49,50,51,52,53,],[29,-29,-33,-32,29,-34,-27,-28,-30,-31,]),'MINUS':([7,9,11,15,20,27,49,50,51,52,53,],[30,-29,34,-33,-32,30,-34,-27,-28,-30,-31,]),'TIMES':([9,15,20,49,50,51,52,53,],[31,-33,-32,-34,31,31,-30,-31,]),'DIVIDE':([9,15,20,49,50,51,52,53,],[32,-33,-32,-34,32,32,-30,-31,]),'QUESTION':([12,],[35,]),'RBRACKET':([21,22,23,24,25,26,44,45,46,47,48,],[43,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,]),'LINE':([34,],[54,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stament':([0,],[1,]),'vector':([0,17,18,19,],[3,40,41,42,]),'compute':([2,],[6,]),'expression':([2,5,],[7,27,]),'function':([2,],[8,]),'term':([2,5,29,30,],[9,9,50,51,]),'factor':([2,5,29,30,31,32,],[20,20,20,20,52,53,]),'multipleObjects':([4,42,],[21,59,]),'multiplestring':([13,],[36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stament","S'",1,None,None,None),
  ('stament -> LPAREN compute RPAREN','stament',3,'p_stament','sintactico_clojure.py',6),
  ('stament -> vector','stament',1,'p_stament','sintactico_clojure.py',7),
  ('compute -> expression','compute',1,'p_compute','sintactico_clojure.py',12),
  ('compute -> function','compute',1,'p_compute','sintactico_clojure.py',13),
  ('function -> FUNCTION_PRINTLN STRING','function',2,'p_function_println','sintactico_clojure.py',18),
  ('function -> READ MINUS LINE','function',3,'p_function_readLine','sintactico_clojure.py',22),
  ('function -> FUNCTION_EMPTY QUESTION STRING','function',3,'p_function_empty','sintactico_clojure.py',25),
  ('multiplestring -> STRING','multiplestring',1,'p_multiplestring','sintactico_clojure.py',28),
  ('multiplestring -> multiplestring STRING','multiplestring',2,'p_multiplestring','sintactico_clojure.py',29),
  ('function -> TYPE_STR multiplestring','function',2,'p_function_concant','sintactico_clojure.py',32),
  ('function -> FUNCTION_SUB STRING NUMBER','function',3,'p_function_subString','sintactico_clojure.py',35),
  ('function -> FUNCTION_SEQ STRING','function',2,'p_function_sequence','sintactico_clojure.py',38),
  ('multipleObjects -> STRING','multipleObjects',1,'p_multipleObjects','sintactico_clojure.py',42),
  ('multipleObjects -> NUMBER','multipleObjects',1,'p_multipleObjects','sintactico_clojure.py',43),
  ('multipleObjects -> FLOAT','multipleObjects',1,'p_multipleObjects','sintactico_clojure.py',44),
  ('multipleObjects -> BOOLEAN_TRUE','multipleObjects',1,'p_multipleObjects','sintactico_clojure.py',45),
  ('multipleObjects -> BOOLEAN_FALSE','multipleObjects',1,'p_multipleObjects','sintactico_clojure.py',46),
  ('multipleObjects -> multipleObjects STRING','multipleObjects',2,'p_multipleObjects','sintactico_clojure.py',47),
  ('multipleObjects -> multipleObjects NUMBER','multipleObjects',2,'p_multipleObjects','sintactico_clojure.py',48),
  ('multipleObjects -> multipleObjects FLOAT','multipleObjects',2,'p_multipleObjects','sintactico_clojure.py',49),
  ('multipleObjects -> multipleObjects BOOLEAN_TRUE','multipleObjects',2,'p_multipleObjects','sintactico_clojure.py',50),
  ('multipleObjects -> multipleObjects BOOLEAN_FALSE','multipleObjects',2,'p_multipleObjects','sintactico_clojure.py',51),
  ('vector -> LBRACKET multipleObjects RBRACKET','vector',3,'p_vector','sintactico_clojure.py',54),
  ('function -> FUNCTION_GET vector NUMBER','function',3,'p_function_get','sintactico_clojure.py',58),
  ('function -> FUNCTION_COUNT vector','function',2,'p_function_count','sintactico_clojure.py',61),
  ('function -> FUNCTION_CONJ vector multipleObjects','function',3,'p_function_conj','sintactico_clojure.py',64),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintactico_clojure.py',68),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintactico_clojure.py',72),
  ('expression -> term','expression',1,'p_expression_term','sintactico_clojure.py',76),
  ('term -> term TIMES factor','term',3,'p_term_times','sintactico_clojure.py',80),
  ('term -> term DIVIDE factor','term',3,'p_term_div','sintactico_clojure.py',84),
  ('term -> factor','term',1,'p_term_factor','sintactico_clojure.py',88),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico_clojure.py',92),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintactico_clojure.py',96),
]

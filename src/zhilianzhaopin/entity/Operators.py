from typing import Dict


class Operators:
    AND = "&&"
    AND_NOT = "!"
    ARRAY_END = ']'
    ARRAY_END_STR = "]"
    ARRAY_SEPRATOR = ','
    ARRAY_SEPRATOR_STR = ","
    ARRAY_START = '['
    ARRAY_START_STR = "["
    BLOCK_END = '}'
    BLOCK_END_STR = "}"
    BLOCK_START = '{'
    BLOCK_START_STR = "{"
    BRACKET_END = ')'
    BRACKET_END_STR = ")"
    BRACKET_START = '('
    BRACKET_START_STR = "("
    CONDITION_IF = '?'
    CONDITION_IF_MIDDLE = ':'
    CONDITION_IF_STRING = "?"
    DIV = "/"
    DOLLAR = '$'
    DOLLAR_STR = "$"
    DOT = '.'
    DOT_STR = "."
    EQUAL = "==="
    EQUAL2 = "=="
    G = ">"
    GE = ">="
    KEYWORDS:Dict[str, object] = {}
    L = "<"
    LE = "<="
    MOD = "%"
    MUL = "*"
    NOT_EQUAL = "!=="
    NOT_EQUAL2 = "!="
    OPERATORS_PRIORITY:Dict[str,str] = {}
    OR = "||"
    PLUS = "+"
    QUOTE = '\"'
    SINGLE_QUOTE = '\''
    SPACE = ' '
    SPACE_STR = " "
    SUB = "-"

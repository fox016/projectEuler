def semantic(ast):
	print ast

ast = "PROGRAM\n    DECLARATION\n        VARIABLE\n            a\n        integer\n    IF\n        CONSTANT\n            1\n        ASSIGNMENT\n            VARIABLE\n                a\n            CONSTANT\n                2\n"
semantic(ast)

BREAKABLES = {}
BREAKABLES['carrot plant'] = {'break type': 'sudden', 'wobble': True, 'weapon required': 'sword', 'animate speed': 50, 'right weapon hit sound': 'rustle', 'hit sound': 'rustle', 'break sound': 'rustle', 'health': 1, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': True, 'items': {'carrot':2}, 'rare items': ['green moth']}
BREAKABLES['potato bush'] = {'break type': 'sudden', 'wobble': True, 'weapon required': 'sword', 'animate speed': 50, 'right weapon hit sound': 'rustle', 'hit sound': 'rustle', 'break sound': 'rustle', 'health': 2, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': True, 'items': {'potato':3}, 'rare items': ['red crystal', 'rabbit', 'green moth', 'snake', 'garden lizard']}
BREAKABLES['iron vein'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'iron ore':4}, 'rare items': [None]}
BREAKABLES['gold vein'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'gold ore':4}, 'rare items': [None]}
BREAKABLES['silver vein'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'silver ore':4}, 'rare items': [None]}
BREAKABLES['aluminum vein'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'aluminum ore':4}, 'rare items': [None]}
BREAKABLES['tin vein'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'tin ore':4}, 'rare items': [None]}
BREAKABLES['copper vein'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'copper ore':4}, 'rare items': [None]}
BREAKABLES['breakable rock'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'ordinary rock':4}, 'rare items': ['flint stone']}
BREAKABLES['breakable wall'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'pickaxe', 'animate speed': 50, 'right weapon hit sound': 'pickaxe', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 4, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'brick':6}, 'rare items': [None]}
BREAKABLES['empty turtle shell'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'mace', 'animate speed': 50, 'right weapon hit sound': 'rock_hit', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 2, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': True, 'items': {'turtle shell plate':12}, 'rare items': ['bluefish']}
BREAKABLES['large dead tree'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'axe', 'animate speed': 70, 'right weapon hit sound': 'rock_hit', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 5, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'cut wood':12}, 'rare items': ['dead brown bird']}
BREAKABLES['small dead tree'] = {'break type': 'gradual', 'wobble': False, 'weapon required': 'axe', 'animate speed': 70, 'right weapon hit sound': 'rock_hit', 'hit sound': 'rock_hit', 'break sound': 'rocks', 'health': 3, 'damage': 0, 'knockback': 0, 'protected': False, 'random drop number': False, 'items': {'cut wood':5}, 'rare items': ['dead brown bird']}


VEIN_LIST = []
for item in BREAKABLES:
    if 'vein' in item:
        VEIN_LIST.append(item)
    if 'rock' in item:
        VEIN_LIST.append(item)

TREE_LIST = []
for item in BREAKABLES:
    if 'tree' in item:
        TREE_LIST.append(item)

PLANT_LIST = []
for item in BREAKABLES:
    if 'plant' in item:
        PLANT_LIST.append(item)
    if 'bush' in item:
        PLANT_LIST.append(item)


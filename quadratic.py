# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    root = b**2 - 4*a*c
    if root < 0:
        return "( )"
    elif root == 0:
        root2 = -1*b / 2*a
        return f"({root2})"
    elif root > 0:
        root = root**0.5
        root3 = (-1*b + root)/(2*a)
        root4 = (-1*b - root)/(2*a)
        return f"({root3}, {root4})"

def value_y(a, b, c, x):
    equation = a*(x**2) + b*x + c
    return equation

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0 and a != 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    dera = a*2
    if dera == 0 and b != 0:
        return f"f'(x) = {b}"
    elif dera != 0 and b != 0:
        return f"f'(x) = {dera} * X + {b}"
    elif dera == 0 and b == 0:
        return f"f'(x) = 0"
    elif dera != 0 and b == 0:
        return f"f'(x) = {dera} * X"

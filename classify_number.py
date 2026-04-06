# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):
    if n == 0:
        return "zero"
    elif is_positive(n) == True and is_even(n) == True:
        return "positive even"
    elif is_positive(n) == True and is_even(n) == False:
        return "positive odd"
    elif is_positive(n) == False and is_even(n) == True:
        return "negative even"
    elif is_positive(n) == False and is_even(n) == False:
        return "negative odd"

# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    vowel = count_vowels(text)
    consonant = count_consonants(text)
    letter = vowel + consonant
    return letter
    
    """
    Retorna la cantidad total de letras en el texto.
    Debe USAR las funciones count_vowels y count_consonants.
    """


def vowel_percentage(text):
    letter = total_letters(text)
    vowel = count_vowels(text)
    if letter == 0:
        return 0.0
    else:
        percentage = round(float((vowel / letter) * 100), 1)
        return percentage
    
    """
    Retorna el porcentaje de vocales sobre el total de letras, redondeado a 1 decimal.
    Si no hay letras, retorna 0.0.
    Debe USAR las funciones count_vowels y total_letters.

    Ejemplo: "hola" tiene 2 vocales de 4 letras → 50.0
    """

def analyze_text(text):
    vowelq = count_vowels(text)
    consonantq = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)
    return f"V:{vowelq} C:{consonantq} T:{total} P:{percentage}%"
    
    """
    Retorna un string con el análisis completo del texto usando el siguiente formato:
    "V:{vowels} C:{consonants} T:{total} P:{percentage}%"

    Debe USAR las funciones count_vowels, count_consonants, total_letters y vowel_percentage.

    Ejemplo: analyze_text("hola") → "V:2 C:2 T:4 P:50.0%"
    """

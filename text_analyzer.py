# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
#count_vowels()

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count
#count_consonants()

# ---- Funciones a implementar ----

def total_letters(text):
    vowel = count_vowels(text)
    consonant = count_consonants(text)
    letter = vowel + consonant
    return letter
#total_letters()

def vowel_percentage(text):
    letter = total_letters(text)
    vowel = count_vowels(text)
    if letter == 0:
        return 0.0
    else:
        percentage = round(float((vowel / letter) * 100), 1)
        return percentage
#vowel_percentage()

def analyze_text(text):
    vowelq = count_vowels(text)
    consonantq = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)
    return f"V:{vowelq} C:{consonantq} T:{total} P:{percentage}%"
#analyze_text()
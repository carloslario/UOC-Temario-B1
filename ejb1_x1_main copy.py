from util_package import text_manager 
from util_package.text_manager import TEXT, is_newline, is_space, remove_punctuation_marks

def find_largest_word(text):
    text = remove_punctuation_marks(text)
    word = max_word = ""
    cont = max_count = 0
    for n in text:
        if is_newline(n) or is_space(n):
            if cont >= max_count:
                max_word = word
                max_count = cont
                cont = 0
                word = ""
            else:
                cont = 0
                word = ""
        else:
            cont += 1
            word += n
    if cont > max_count:
        max_word = word
    return max_word

def is_palindrome_word(word):
    if len(word) <= 1:
        return True
    else:
        return word[0].lower() == word[-1].lower() and is_palindrome_word(word[1:-1])


def count_palindrome_words(text):
    text = remove_punctuation_marks(text)
    pal_count = 0
    word = ""
    for n in text:
        if is_newline(n) or is_space(n):
            if word:
                if is_palindrome_word(word):
                    pal_count += 1
                    word = ""
                else:
                    word = ""
        else:
            word += n
    if word and is_palindrome_word(word):
        pal_count += 1
    return pal_count

def find_size_largest_sentence(text, filter):
    count = max_count = 0
    stnce = max_stnce = ""

    for n in text:
        if is_newline(n):
            if count >= max_count and filter in stnce:
                max_stnce = stnce
                max_count = count
                stnce = ""
                count = 0
            else:
                stnce = ""
                count = 0
        else:
            stnce += n
            count += 1

    if count >= max_count and filter in stnce:
        max_stnce = stnce
        max_count = count

    if max_count == 0:
        raise ValueError(f"Ninguna frase coincide con el filtro '{filter}'")

    return max_count
    


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
"""
print("La palabra mas larga es:", find_largest_word(TEXT))
print("'aa' es un palíndromo su resultado es:", is_palindrome_word("aa"))
print("'abx' no un palíndromo su resultado es:", is_palindrome_word("abx"))
print("'a' es un palíndromo su resultado es:", is_palindrome_word("a"))
print("'Ababa' es palíndromo su resultado es:", is_palindrome_word("Ababa"))
print("El número de palabras identificadas como palíndromos es:", count_palindrome_words(TEXT))
print("El tamaño de la oración más larga con el filtro='a', es :", find_size_largest_sentence(TEXT, "a"))
"""
# Rules
# Якщо літера на початку Є -> Ye, Ї -> Yi, Ю -> Yu, Я -> Ya
# В усіх випадках зг -> zgh

cyrillic_to_latin_first_letter_exceptions = {
    "є": 'ye', 'ї': 'yi', 'ю': 'yu', 'я': 'ya',
    "Є": 'Ye', 'Ї': 'Yi', 'Ю': 'Yu', 'Я': 'Ya'
}

cyrillic_to_latin_small_dict = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e',
    'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i',
    'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ю': 'iu', 'я': 'ia',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E',
    'Є': 'Ie', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'I', 'Й': 'I',
    'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
    'Ш': 'Sh', 'Щ': 'Shch', 'Ю': 'Iu', 'Я': 'Ia'
}

def translit_from_ukr_to_eng(delimiter=" ", text_to_translit=""):
    temp_words_list = text_to_translit.split(delimiter)

    # Step 0: translit "зг" to "zgh" for all words
    temp_words_list = [word.replace("зг", "zgh") for word in temp_words_list]
    temp_words_list = [word.replace("Зг", "Zgh") for word in temp_words_list]

    # Step 1: translit exception first letter for all words
    temp_words_list = [
        word[0].translate(
            str.maketrans(cyrillic_to_latin_first_letter_exceptions)
        ) + word[1:len(word)] for word in temp_words_list
    ]

    # Step 2: translit everything else
    temp_words_list = [
        word.translate(
            str.maketrans(cyrillic_to_latin_small_dict)
        ) for word in temp_words_list
    ]

    return " ".join(temp_words_list)

cyrillic_text = "Привіт друже, як ти? Їси яблука? А для мене в Юлі ще є? Згодом наберу."
print(translit_from_ukr_to_eng(text_to_translit=cyrillic_text))

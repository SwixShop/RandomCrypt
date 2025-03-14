languages = {
    "ru": [i for i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"],
    "en": [i for i in "abcdefghijklmnopqrstuvwxyz"]
}
def crypt(text: str, lang: str = "ru", sdvig: int = 0) -> str:
    """lang: ru, en """
    string = ""
    before = 0
    for symbol in text.lower():
        if symbol in languages[lang]:
            string += languages[lang][(languages[lang].index(symbol) + before + sdvig) % len(languages[lang])]
            before += languages[lang].index(symbol) + int(sdvig ** 0.5)
        else:
            string += symbol
    return string.capitalize()

def decrypt(text: str, lang: str = "ru", sdvig: int = 0) -> str:
    """lang: ru, en """
    string = ""
    before = 0
    for symbol in text.lower():
        if symbol in languages[lang]:
            string += languages[lang][(languages[lang].index(symbol) - before - sdvig) % len(languages[lang])]
            before += languages[lang].index(languages[lang][(languages[lang].index(symbol) - before - sdvig) % len(languages[lang])]) + int(sdvig ** 0.5)
        else:
            string += symbol
    return string.capitalize()

print(crypt("Красная машина!!!", "ru", 100))
print(decrypt("Лёпквлф кфциай!!!", "ru", 100))
print(crypt("Hello, world!", "en", 5))
print(decrypt("Msfsi, gwpch!", "en", 5))
print("Смотри! Там пробежала черная кошка, тудой не идем. ->", crypt("Смотри! Там пробежала черная кошка, тудой не идем.", "ru", 100))

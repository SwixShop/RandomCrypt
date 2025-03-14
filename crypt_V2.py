symbols = [i for i in "puёрog9G^lф`(ИФПJДBЖAяM@._CУ+&ЩбМESВЕ#ЬWЫmезI-п№2dLyqАwNЦ>йtjв}vkн~у=x)чсKиie,Б0О[Oa1QхzU ЁЙь3дг4шЗ|YЛ$ъжsкСZтРVН!;/о8PЯ5HаnDы7ЮГ{КcЭм*л:<b6ШXf%hщюTrТЧЪ]эRFХц"]

def crypt(text: str, key: str = "", sdvig: int = 0) -> str:ё
    string = ""
    before = 0
    for symbol in text.lower():
        if symbol in symbols:
            string += symbols[(symbols.index(symbol) + before + sdvig) % len(symbols)]
            try:
                before += symbols.index(symbol) + \
                    int(sdvig ** 0.5) * sdvig + \
                    sdvig * symbols.index(symbol) ** 3 * int(before ** 0.5) + \
                    key.index(key[before % len(key)]) ** 2 * before
            except:
                before = 25
        else:
            string += symbol
    return string


def decrypt(text: str, key: str = "", sdvig: int = 0) -> str:
    string = ""
    before = 0
    for symbol in text:
        if symbol in symbols:
            string += symbols[(symbols.index(symbol) - before - sdvig) % len(symbols)]
            try:
                before += symbols.index(symbols[(symbols.index(symbol) - before - sdvig) % len(symbols)]) + \
                    int(sdvig ** 0.5) * sdvig + \
                    sdvig * symbols.index(symbols[(symbols.index(symbol) - before - sdvig) % len(symbols)]) ** 3 * int(before ** 0.5) + \
                    key.index(key[before % len(key)]) ** 2 * before
            except:
                before = 25
        else:
            string += symbol
    return string.capitalize()

print(crypt("Генератор текста — компьютерная программа, генерирующая тексты, корректные с точки зрения большинства языковых норм, но, как правило, лишённые смысла.", "костыли на корточках", 34345))
print(decrypt("RyЛVNX8 лQ+к1CВr6—ПЗйбщЫ@XЧ&NЙ,2xg`umЕN6u +ЧЛ&Уу/nh№бМE9кУ~P>йZ~NqПК0kFйжuрИ№=[ВШRД$с3>щуЫhlnHvсaК62KEР5Б`сГЗyвЯH09pОЁicr|(к0HТя<GzbЦх1u[ncx(sв>|qGnОщ", "костыли на корточках", 34345))

print(crypt("Красная машина!!!", "Красная машина!!!", 100))
print(decrypt("2ъСgЗК жdъ1]-ДкНИ", "Красная машина!!!", 100))

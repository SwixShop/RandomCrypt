sym = [i for i in "puёрog9G^lф`(ИФПJДBЖAяM@._CУ+&ЩбМESВЕ#ЬWЫmезI-п№2dLyqАwNЦ>йtjв}vkн~?у=x)чсKиie,Б0О[Oa1QхzU ЁЙь3дг4шЗ|YЛ$ъжsкСZтРVН!;/о8PЯ5HаnDы7ЮГ{КcЭм*л:<b6ШXf%hщюTrТЧЪ]эRFХц"]

def do_symbols_with_key(array: list, key: str) -> list:
    for i in key:
        if i not in array:
            array.append(i)
    return array


def crypt(text: str, key: str = "", sdvig: int = 0) -> str:
    symbols = do_symbols_with_key(sym.copy(), key)
    key = key + "".join(symbols)[:10]
    sdvig = sdvig + sum(ord(i) ** 2 for i in key)
    string = ""
    before = 0
    for symbol in text:
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
    symbols = do_symbols_with_key(sym.copy(), key)
    key = key + "".join(symbols)[:10]
    sdvig = sdvig + sum(ord(i) ** 2 for i in key)
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
    return string

if __name__ == "__main__":
    print(crypt(input("Напиши что нужно зашифровать: "), input("Напиши ключ шифрования (по дефолту его нет), чем больше букв тем: "), int(input("Какой сдвиг сделать?: "))))

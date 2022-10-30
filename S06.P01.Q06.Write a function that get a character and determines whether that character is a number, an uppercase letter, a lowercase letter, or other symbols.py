#  سید مجتبی موسوی / تکالیف مبحث تابع / سوال 6
#   تابعی بنویسید که یک کاراکتر را خوانده و مشخص کند کاراکتر یک رقم، حرف بزرگ، حرف کوچک و یا سایر نماد ها است

def character_identification(ch):
    if ord(ch) >= 48 and ord(ch) <= 57:
        return "Character is Number"
    elif ord(ch) >= 65 and ord(ch) <= 90:
        return "Character is Capital Letters"
    elif ord(ch) >= 97 and ord(ch) <= 122:
        return "Character is Lowercase Letters"
    else:
        return "Character is Other Letters"


e_ch = input("Type a Character: ")

print(character_identification(e_ch))

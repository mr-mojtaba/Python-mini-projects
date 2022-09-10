# سید مجتبی موسوی / تکالیف مبحث ساختار تصمیم / سوال 3

e = input("Enter one Character : ")

t = ord(e)

if t >= 65 and t <= 90 or t >= 97 and t <= 122:
    print(e, "is a Letters")
elif t >= 48 and t <= 57:
    print(e, "is a Number")
else:
    print("is a Other Symbols ...")
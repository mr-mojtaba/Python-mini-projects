# سید مجتبی موسوی / تکالیف مبحث ژنراتور / سوال 4
# ژنراتوری بنویسید که یک رشته گرفته و معکوس آن را برگرداند.(هر بار یک کاراکتر)

def reverse_gen(enter):
    l = len(enter)
    for i in range(l-1, -1, -1):
        yield enter[i]

st = "salam"

r = reverse_gen(st)

for j in r:
    print(j)
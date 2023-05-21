# سید مجتبی موسوی / تکالیف مبحث ژنراتور / سوال 1
# رفتار enumerate را با استفاده از ژنراتور پیاده سازی کنید.

def egr(enter, strt=1):
    s = strt
    for i in enter:
        yield s, i
        s += 1


l = ["ali", "mamad", "reza"]

for i, j in egr(l):
    print(i, j)

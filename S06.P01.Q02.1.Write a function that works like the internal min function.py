#  سید مجتبی موسوی / تکالیف مبحث تابع / سوال 2.1
#  تابعی بنویسید که کار تابع داخلی min را انجام دهد

def f_min(*args):
    smin = float("+inf")

    for i in args:
        if i < smin:
            smin = i
    return smin


print(f_min(2558, 654, 0, -50))
print(min(2558, 654, 0, -50))

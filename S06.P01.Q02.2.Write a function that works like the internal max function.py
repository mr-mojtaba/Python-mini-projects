# سید مجتبی موسوی / تکالیف مبحث تابع / سوال 2.2
#  تابعی بنویسید که کار تابع داخلی max را انجام دهد

def f_max(*args):
    smax = float("-inf")

    for i in args:
        if i > smax:
            smax = i
    return smax


print(f_max(2558, 654, 0, -50))
print(max(2558, 654, 0, -50))

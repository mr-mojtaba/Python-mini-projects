#  سید مجتبی موسوی / تکالیف مبحث تابع / سوال 1
#  تابعی بنویسید که کار تابع داخلی len را انجام دهد

def f_len(a):
    counter = 0
    for i in a:
        counter += 1
    return counter


w = {"a": 1, "b": 2, "c": 3}

print(f_len(w))
print(len(w))

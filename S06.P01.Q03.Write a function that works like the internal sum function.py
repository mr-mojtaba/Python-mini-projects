#  سید مجتبی موسوی / تکالیف مبحث تابع / سوال 3
#   تابعی بنویسید که که کار تابع داخلی sum را انجام دهد

def f_sum(a):
    sum_list = 0

    for i in a:
        sum_list += i
    return sum_list


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f_sum(l))
print(sum(l))

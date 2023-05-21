# سید مجتبی موسوی / تکالیف مبحث ژنراتور / سوال 6
# ژنراتوری ایجاد کنید که در هر مرحله خروجی های زیر را تولید کند:
# بار اول: 1
# بار دوم: 2 2
# بار سوم: 3 3 3
# و ...

def my_counter():
    my_int = 1
    while True:
        c = ""
        for i in range(1, my_int+1):
            c += f"{my_int}\t"
        yield c
        my_int += 1

s = my_counter()

for i in range(20):
    print(next(s))

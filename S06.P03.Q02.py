# سید مجتبی موسوی / تکالیف مبحث ژنراتور / سوال 2
# یک ژنراتور برای تولید دنباله فیبوناچی بنویسید.

def fibonacci():
    f1 = 0
    yield f1
    f2 = 1
    yield f2
    while True:
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3

fib = fibonacci()

for _ in range(15):
    print(next(fib))

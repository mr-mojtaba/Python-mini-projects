# سید مجتبی موسوی / تکالیف مبحث حلقه و اعداد تصادفی / سوال 4

n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the second Number: "))

mn = min(n1, n2)
mx = max(n1, n2)

for i in range(1, mn+1):
    if mx * i % mn == 0:
        print(mx * i)
        break
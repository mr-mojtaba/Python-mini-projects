# سید مجتبی موسوی / تکالیف مبحث حلقه و اعداد تصادفی / سوال 1

n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the second Number: "))

mn = min(n1, n2)
mx = max(n1, n2)

for i in range(mn, mx+1):
    print(i, end=" ")

# سید مجتبی موسوی / تکالیف مبحث حلقه و اعداد تصادفی / سوال 3

n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the second Number: "))

mn = min(n1, n2)
l = []

for i in range(1, mn+1):
    if n1 % i == 0 and n2 % i == 0:
        l.append(i)
        
print("Greatest common Divisor:", max(l))

# سید مجتبی موسوی / تکالیف مبحث حلقه و اعداد تصادفی / سوال 5

n = int(input("Enter the first Number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1

print("The number of digits is: ", count)

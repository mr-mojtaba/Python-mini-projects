# سید مجتبی موسوی / تکالیف مبحث لامبدا / سوال 4
#  برنامه ای بنویسید تا لیستی از اعداد صحیح را با استفاده از لامبدا به زوج ها و فردها فیلتر کند

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

even = list(filter(lambda x: x % 2 == 0, li))
odd = list(filter(lambda x: x % 2 == 1, li))

print("Even =", even)
print("Odd =", odd)

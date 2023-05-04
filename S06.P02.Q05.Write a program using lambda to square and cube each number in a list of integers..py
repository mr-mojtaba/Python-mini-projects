# سید مجتبی موسوی / تکالیف مبحث لامبدا / سوال 5
#  با استفاده از لامبدا یک برنامه ای بنویسید تا هر عدد را در لیستی از اعداد صحیح مربع و مکعب کند.

li = [2, 4, 6, 8, 10]

square = list(map(lambda x: x ** 2, li))
cube = list(map(lambda x: x ** 3, li))

print("Squares list = ", square)
print("Cubes list = ", cube)

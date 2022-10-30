#  سید مجتبی موسوی / تکالیف مبحث تابع / سوال 5
#  تابعی بنویسید که قیمت کالا و درصد تخفیف را گرفته و قیمت پس از تخفیف را محاسبه کند

def apply_discount(price, discount):
    final_price = (price / 100) * (100 - discount)
    return int(final_price)


e_price = int(input("Enter the price: "))
e_discount_percent = int(input("Enter the discount percent: "))

print("Final Price = ", apply_discount(e_price, e_discount_percent))

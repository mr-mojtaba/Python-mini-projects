#  سید مجتبی موسوی / تکالیف مبحث لامبدا / سوال 3
#  لیستی از دیکشنری ها به شکل [… ,{‘weight’: 50, ‘apple’: ‘red’}] داریم.
#  با استفاده از لامبدا برنامه ای بنویسید که این لیست را بر اساس رنگ موجود در دیکشنری مرتب کند

li = [{"name": "apple", "weight": 100, "color": "red"},
      {"name": "apple", "weight": 120, "color": "white"},
      {"name": "tangerine", "weight": 100, "color": "green"},
      {"name": "tangerine", "weight": 80, "color": "orange"}]

s_li = sorted(li, key=lambda x: x["color"])

print("Sorted List = ", s_li)

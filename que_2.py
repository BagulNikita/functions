#movie tickets prices are based on age group Rs.600 for adult(18 and over)
#and Rs.200 for childrens.Everyoe gets 20rs discount on wednesday.

age=15
day="Wednesday"
price=600 if age>=18 else 200
if day=="Wednesday":
    price=price-20
print("The ticket price for you is Rs.",price)
meal_cost=float(input())
tip_percent=int(input())
tax_percent=int(input())
tip= (meal_cost/100)*tip_percent
tax= (meal_cost/100)*tax_percent
total_cost= meal_cost+tip +tax
print(round(total_cost))
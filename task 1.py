# task 1 1:
principle  = float(input("enter the principle amount:"))
rate = float(input("enter the rate of interest:"))
time = float(input("enter the time in years:"))
compuond_interest = principle*((1+rate/100)*time)-principle 
print("the compound interest is:",compuond_interest)

# task 1 2:
def calculate_total_cost(x,y):
    return x*y
t  = int(input("enter the number of test case:"))
print(calculate_total_cost(5,2))

# task 1 3:
SOFT_PER_ACRE = 43560
length  = float(input("enter the length of the field in feet:"))
width = float(input("enter the width of the field in feet:"))
area_sqft = length*width
acres = area_sqft / SOFT_PER_ACRE
print("the area of the field is",acres,"acres")

# task 1 4:
import math
def calculate_area_in_acres(radius_in_feet):
    area_in_acres = math.pi*(radius_in_feet**2)/43560
    return area_in_acres
radius_in_feet = float(input("enter the radius of the field in feet:"))
area_in_acres = calculate_area_in_acres(radius_in_feet)
print(f"the ares of the field is :{area_in_acres:.2f} acres")

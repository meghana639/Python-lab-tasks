# task 3 1:
import datetime
input_date = input("enter the date in MM DD YYYY format: ")
month,day,year = map(int,input_date.split())
if 2000<=year<=3000:
    x = datetime.datetime(year,month,day)
    day_name = x.strftime("%A").upper()
    print(day_name)
else:
    print("year is not within the specified constraints:")


# task 3 2:
def compute_armstrong(x):
    n = len(str(x))
    return sum(int(i) ** n for i in str(x)) == x

number = int(input("Enter a number: "))
if compute_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

# task 3 3:
import math
def euclidean_distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
X = (1, 3)
Y = (2, 3)
result = euclidean_distance(X, Y)
print("Euclidean distance between X and Y:", result)

# task 3 4:
def display():
    print("hello world")

def sum(a, b):
    return a + b

display()
res = sum(1, 2)
print(res)

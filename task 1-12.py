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

# task 2 1:
import random

def guess_number():
    target_number = random.randint(1, 9)
    while True:
        user_guess = int(input("Guess a number between 1 and 9: "))
        if user_guess == target_number:
            print("Well guessed!")
            break
        else:
            print("Wrong guess. Try again.")

guess_number()


# task 2 2:
for number in range(1, 51):
 if number % 3 == 0 and number % 5 == 0:
  print("FizzBuzz")
 elif number % 3 == 0:
  print("Fizz")
 elif number % 5 == 0:
  print("Buzz")
 else:
  print(number)

# task 2 3:
nums = list(input("Enter a sequence of comma-separated 4-digit binary numbers: ").split(','))
res = [i for i in nums if int(i, 2) % 6==0]
print(res)  

# task 2 4:
def count_even_odd(numbers):
 even_count = 0
 odd_count = 0
 for num in numbers:
  if num % 2 == 0:
   even_count += 1
  else:
   odd_count += 1
 return even_count, odd_count
input_numbers = input("Enter a series of numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))
even_count, odd_count = count_even_odd(numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

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

# task 4 1:
sample = []
sample.insert(0,12)
print(sample)
sample.insert(1,4)
print(sample)
sample.insert(2,2)
print(sample)
sample.insert(3,4)
print(sample)
sample.remove(4)
print(sample)
sample.append(21)
print(sample)
sample.sort()
print(sample)
sample.pop()
print(sample)
sample.reverse()
print(sample)
a = list(range(10))
print(a)

# task 4 2:
alist = []
for i in range(int(input("Enter number of students: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    alist.append([name, score])
scores = sorted(set([score for name, score in alist]))
second_lowest = scores[1]
names = [name for name, score in alist if score == second_lowest]
for name in sorted(names):
    print(name)

# task 4 3:
n = int(input())    
a = map(int, input().split()) 
t = tuple(a)                  
print(hash(t))   

# task 4 4:
def min_paint_balloons(s):
    amber_count = s.count('a')
    brass_count = s.count('b')
    min_part = min(amber_count,brass_count)
    return min_part
T = int(input("enter the total testcases"))
for i in range(T):
    S = input().strip()
    print(min_paint_balloons(S))

# task 5 1:
def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1    
arr = [10,20,80,30,60,50,110,100,130,170]
x = 110
result = search(arr,x)
if result != -1:
    print("element",x,"is present at index",result)
else:
    print("element",x,"is not present in the array")   

# task 5 2:
def binary_search(nums,target):
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = left+(right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid - 1
    return -1
nums = [-1,0,3,5,9,12]
target = 9
print(binary_search(nums,target))               


# task 5 3:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
def find_sequence(arr):
    smallest = arr[0]
    largest = arr[-1]
    print("sequence of integers:",smallest,"to",largest)
n = int(input("enter the number of integers:"))
integers = []
print("enter the integers:")
for _ in range(n):   
    integers.append(int(input()))
bubble_sort(integers)
find_sequence(integers)  


# task 5 4:
def selection_sort(scores):
    n = len(scores)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if scores[j]<scores[min_index]:
                min_index = j
        scores[i],scores[min_index] = scores[min_index],scores[i]
        print("after iteration",i+1,":",scores)
exam_scores = [87,65,92,78,55,70,82]
print("initial exam scores:",exam_scores)
print("sorting using selection sort:")
selection_sort(exam_scores)
print("final sorted exam scores:",exam_scores)                


# task 6 1:
def copy_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path,'r') as original_file:
                orginal_content = original_file.read()
                copy_file_path = file_path.split('.')[0] + '_copy.' + file_path.split('.')[1]
                with open(copy_file_path,'w') as copy_file:
                    copy_file.write(orginal_content)
                print(f"contents copied from{file_path} to {copy_file_path} successfully.")
        else:
            print(f"Error: File'{file_path}'not found.")   
import os
file_list = ['file1.txt','file2.txt','file2.txt']
copy_files(file_list)                 


# task 6 2:
def create_file_and_count_occurances():
    file_name = input("enter the file name to create: ")
    with open(file_name,'w') as file:
        print("enter the contents of the file(press enter to finish): ")
        while True:
            line = input()
            if not line:
                break
            file.write(line + '\n')
    print("\ncontents of the file:")
    with open(file_name,'r') as file:
        print(file.read())
    letter = input("\nenter the letter to count occurences:")
    with open(file_name,'r') as file:
        content = file.read()
        count = content.count(letter)
        print(f"\nThe letter'{letter}'occurs{count}times in the file.")
create_file_and_count_occurances()                    


# task 6 3:
def create_file_and_count_words():
    file_name = input("enter the file name to create:")
    with open(file_name,'w') as file:
        print("enter the contents of the file(press enter to finish:)")
        while True:
            line = input()
            if not line:
                break
            file.write(line+'\n')
    print('\ncontents of the file:')
    with open(file_name,'r') as file:
        print(file.read())
    with open(file_name,'r') as file:
        content = file.read()
        word_count = len(content.split())
        print(f"\nThe number of words in the file is:{word_count}")
create_file_and_count_words()        
                    

# task 6 4:
import csv
with open('apple_quality.csv','r') as file:
    data=csv.reader(file)
    for row in data:
        print(row)

# task 7 1:
def find_discount(qty):
    if qty <= 10:
        return 0
    elif 11 <= qty <= 20:
        return 15
    else:
        return 20
def buy():
    icode = int(input("ener item code:"))
    item = input("enter item name:")
    price = float(input("enter price:"))
    Qty = int(input("enter quantity:"))
    discount = find_discount(Qty)
    netprice = price * Qty - discount
    return icode,item,price,Qty,discount,netprice
def show_all(icode,item,price,Qty,discount,netprice):
    print("item code:",icode)
    print("item:",item)
    print('price:',price)
    print("quantity:",Qty)
    print("discount:",discount)
    print("net price:",netprice)
icode,item,price,Qty,discount,netprice = buy()
show_all(icode,item,price,Qty,discount,netprice)       

# task 7 2:
def cube_of_numbers(n):
    product = 1
    for i in range(1,n+1):
        product *= i**3
    return product
n = int(input("enter the value of n:"))
result = cube_of_numbers(n)
print("cube product of the first",n,"natural numbers is:",result)

# task 7 3:
def func_compute(n):
    return lambda x:x*n
result = func_compute(2)
print("double the number of 15 = ",result(15))
result = func_compute(3)
print("triple the number of 15 = ",result(15))
result = func_compute(4)
print("quadraple the number of 15 = ",result(15))
result = func_compute(5)
print("quantiple the number of 15 = ",result(15))

# task 7 4:
def categorize_tickets(ticket_ids):
    adult_tickets = list(filter(lambda x:x%2==0,ticket_ids))
    child_tickets = list(filter(lambda x:x%2!=0,ticket_ids))
    return adult_tickets,child_tickets
ticket_ids = [101,202,305,410,513,620,723,830,945,1050]
adult_tickets,child_tickets = categorize_tickets(ticket_ids)
print("adult tickets:",adult_tickets)
print("child tickets:",child_tickets)

# task 8 1:
def fibonacci():
 a, b = 0, 1
 for _ in range(10): 
  yield a
 a, b = b, a + b
fibonacci_series = fibonacci() 
for number in fibonacci_series: 
 print(number, end=" ")

# task 8 2:
def squares():
 for i in range(5): 
  yield i ** 2
squares_generator = squares()
for square in squares_generator:
 print(square)

# task 8 3:
def operation_decorator(func):
 def wrapper(x, y):
  print("Performing arithmetic operation...")
 result = func(x, y)
 print("Operation completed.")
 return result
 return wrapper
@operation_decorator
def add(x, y):
 return x + y
@operation_decorator
def divide(x, y):
 if y == 0:
  return "Cannot divide by zero!"
 else:
  return x / y
result_add = add(5, 3)
print("Result of addition:", result_add)
result_divide = divide(15, 0)
print("Result of division:", result_divide)

# task 9 1:
def get_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return age
        except ValueError as ve:
            print("Invalid input:", ve)

try:
    age = get_age()
    print("Your age is:", age)
except ValueError as ve:
    print("An error occurred:", ve)

# task 9 2:
def view_seat_details(seat_list, index):
 try:
  seat = seat_list[index]
  print("Seat Details:")
  print("Seat Number:", seat.get("number"))
  print("Section:", seat.get("section"))
  print("Availability:", "Booked" if seat.get("is_booked") else "Available")
 except IndexError:
  print("Invalid seat index. Please select a valid seat.")
seats = [
 {"number": "A1", "section": "VIP", "is_booked": False},
 {"number": "A2", "section": "VIP", "is_booked": True},
 {"number": "B1", "section": "General", "is_booked": False},
 {"number": "B2", "section": "General", "is_booked": False}
]
try:
 seat_index = int(input("Enter the index of the seat you want to view: "))
 view_seat_details(seats, seat_index)
except ValueError:
 print("Invalid input. Please enter a valid seat index (integer).")    

# task 9 3:
def open_file(filename):
 try:
  file = open(filename, 'r')
  contents = file.read()
  print("File contents:")
  print(contents)
  file.close()
 except FileNotFoundError:
  print("Error: File not found.")
file_name = input("Input a file name: ")
open_file(file_name)

# task 9 4:
try:
 initial_investment = float(input("Enter the initial investment amount: "))
 final_investment = float(input("Enter the final investment amount: "))
 roi = (final_investment - initial_investment) / initial_investment * 100
 print("Return on Investment (ROI): {:.2f}".format(roi))
except ValueError:
 print("Error: Please enter a valid numeric value for the investment amount.")
except ZeroDivisionError:
 print("Error: Initial investment amount cannot be zero.")

# task 10 1:
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 1000) 
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True) 
plt.show() 

# task 10 2:
import matplotlib.pyplot as plt
intervals = ['140-145', '145-150', '151-156', '157-162', '163-168', '168-173', '173-178', '179-184', 
'185-190', '190-195']
frequencies = [2, 5, 15, 31, 46, 53, 45, 28, 21, 4]
plt.bar(intervals, frequencies, edgecolor='red')
plt.xlabel('Height Intervals (cm)')
plt.ylabel('Frequency')
plt.title('Height Distribution Histogram')
plt.grid(True)
plt.show()

# task 10 3:
import matplotlib.pyplot as plt
x= [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y, color='blue')
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.title('Scatter Plot')
plt.show()

# task 10 4:
import matplotlib.pyplot as plt
sizes = [35, 25, 25, 15]
mylabels = ['w', 'x', 'y', 'z']
myexplode = [0.2, 0, 0, 0]
plt.pie(sizes, labels=mylabels, explode=myexplode, shadow = True, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

# task 11 1:
import tkinter as tk
from datetime import datetime

def calculate_age():
    today = datetime.now()
    birth_date = datetime(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_label.config(text=f"Your age is {age}")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Name:",width=50).pack()   
name_entry = tk.Entry(root)  
name_entry.pack()    

tk.Label(root, text="Year of Birth:").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Label(root, text="Month of Birth:").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Day of Birth:").pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Button(root, text="Calculate Age", background='pink',foreground='black',command=calculate_age).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop() 

# task 11 2:
import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

style = "calibri"
size = 40
font_style = (style, size, "bold")

time_label = tk.Label(root, font=font_style, anchor="center", background='purple',foreground='white')  
time_label.pack(fill=tk.BOTH, expand=True) 

update_time()
root.mainloop()

# task 12 1:
import pygame
import random

pygame.init()  
white = (255, 255, 255)       
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

window_width = 600    
window_height = 500
brick_width = 60
brick_height = 20

fps = 60

window = pygame.display.set_mode((window_width, window_height))  
pygame.display.set_caption("Breakout Game")  

paddle = pygame.Rect(window_width // 2 - 50, window_height - 30, 100, 10) 
paddle_speed = 7  

ball = pygame.Rect(window_width // 2 - 10, window_height // 2 - 10, 20, 20)
ball_speed_x = 5 * random.choice((1, -1)) 
ball_speed_y = -5

brick_rows = 5 
brick_columns = 10
bricks = []
for row in range(brick_rows):
    brick_row = []
    for col in range(brick_columns):
        brick = pygame.Rect(col * (brick_width + 10) + 35, row * (brick_height + 5) + 35, brick_width, brick_height)
        brick_row.append(brick) 
    bricks.append(brick_row) 

def draw_bricks():		
    for row in bricks:
        for brick in row:
            pygame.draw.rect(window, blue, brick)

def move_ball():    
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0 or ball.right >= window_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    if ball.colliderect(paddle):
        ball_speed_y *= -1

    for row in bricks:
        for brick in row:
            if ball.colliderect(brick):
                row.remove(brick)
                ball_speed_y *= -1
                break

    if ball.bottom >= window_height:
        return False  
    return True

def display_text(text, size, color, x, y):             
    font = pygame.font.SysFont("comicsansms", size)
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y)) 

def breakout_game():
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < window_width:
            paddle.x += paddle_speed

        if not move_ball():
            display_text("Game Over!", 50, red, window_width // 2 - 130, window_height // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        if all(len(row) == 0 for row in bricks):
            display_text("You Win!", 50, green, window_width // 2 - 130, window_height // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        window.fill(black)

        pygame.draw.rect(window, white, paddle)

        pygame.draw.ellipse(window, red, ball)

        draw_bricks()

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()

breakout_game()

# task 12 2:
import pygame
import time
pygame.init()
WIDTH, HEIGHT = 540, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
font = pygame.font.SysFont("comicsans", 40)  
small_font = pygame.font.SysFont("comicsans", 20)
board = [                                   
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
def draw_grid():    			
    gap = WIDTH // 9 
    for i in range(10):
        if i % 3 == 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(win, BLACK, (0, i * gap), (WIDTH, i * gap), thick)
        pygame.draw.line(win, BLACK, (i * gap, 0), (i * gap, WIDTH), thick)
def draw_numbers(board):                        
    gap = WIDTH // 9
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                win.blit(text, (j * gap + 15, i * gap + 15))
def draw_selected(row, col):  			
    gap = WIDTH // 9
    pygame.draw.rect(win, BLUE, (col * gap, row * gap, gap, gap), 4)
def main():   
    key = None
    row = -1
    col = -1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board[row][col] = 0
                    key = None
                if event.key == pygame.K_RETURN:
                    key = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // (WIDTH // 9)
                col = pos[0] // (WIDTH // 9)
        win.fill(WHITE)
        draw_grid()
        draw_numbers(board)
        if row >= 0 and col >= 0:
            draw_selected(row, col)
        if key is not None and row >= 0 and col >= 0:
            board[row][col] = key
        pygame.display.update()
main()
pygame.quit()



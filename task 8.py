#task 8 1:
def fibonacci():
 a, b = 0, 1
 for _ in range(10): 
  yield a
 a, b = b, a + b
fibonacci_series = fibonacci() 
for number in fibonacci_series: 
 print(number, end=" ")

#task 8 2:
def squares():
 for i in range(5): 
  yield i ** 2
squares_generator = squares()
for square in squares_generator:
 print(square)

#task 8 3:
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

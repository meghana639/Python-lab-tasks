#task 2 1:
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


#task 2 2:
for number in range(1, 51):
 if number % 3 == 0 and number % 5 == 0:
  print("FizzBuzz")
 elif number % 3 == 0:
  print("Fizz")
 elif number % 5 == 0:
  print("Buzz")
 else:
  print(number)

#task 2 3:
nums = list(input("Enter a sequence of comma-separated 4-digit binary numbers: ").split(','))
res = [i for i in nums if int(i, 2) % 6==0]
print(res)  

#task 2 4:
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

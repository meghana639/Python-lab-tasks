#task 9 1:
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

#task 9 2:
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

#task 9 3:
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

#task 9 4:
try:
 initial_investment = float(input("Enter the initial investment amount: "))
 final_investment = float(input("Enter the final investment amount: "))
 roi = (final_investment - initial_investment) / initial_investment * 100
 print("Return on Investment (ROI): {:.2f}".format(roi))
except ValueError:
 print("Error: Please enter a valid numeric value for the investment amount.")
except ZeroDivisionError:
 print("Error: Initial investment amount cannot be zero.")

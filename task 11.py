#task 11 1:
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

#task 11 2:
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

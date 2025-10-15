#task 10 1:
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

#task 10 2:
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

#task 10 3:
import matplotlib.pyplot as plt
x= [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y, color='blue')
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.title('Scatter Plot')
plt.show()

#task 10 4:
import matplotlib.pyplot as plt
sizes = [35, 25, 25, 15]
mylabels = ['w', 'x', 'y', 'z']
myexplode = [0.2, 0, 0, 0]
plt.pie(sizes, labels=mylabels, explode=myexplode, shadow = True, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

#task 4 1:
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

#task 4 2:
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

#task 4 3:
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

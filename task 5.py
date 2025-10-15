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


#task 5 3:
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

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

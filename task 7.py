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

#task 7 4:
def categorize_tickets(ticket_ids):
    adult_tickets = list(filter(lambda x:x%2==0,ticket_ids))
    child_tickets = list(filter(lambda x:x%2!=0,ticket_ids))
    return adult_tickets,child_tickets
ticket_ids = [101,202,305,410,513,620,723,830,945,1050]
adult_tickets,child_tickets = categorize_tickets(ticket_ids)
print("adult tickets:",adult_tickets)
print("child tickets:",child_tickets)

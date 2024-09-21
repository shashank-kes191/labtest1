import numpy as np
import matplotlib.pyplot as ply

arr = np.array([["a", 50, 20],["b", 25, 15],["c", 100,20]])
total_sale = 0

def add_item(arr):
    med = input("Medicine name : ")
    price = input("price : ")
    quan = input("Quantity : ")
    row = np.array([med,int(price),int(quan)])
    arr = np.append( arr ,[row],axis=0)
    
def sales(arr , total_sale):
    x = input("Enter medicine sold : ")
    y = input("Enter quantity sold : ")
    for item in arr:
        if(item[0] == x):
            item[2] -= int(y)    
            total_sale += (int(y) * item[1])

def sale_profit(arr, total_sale):
    print("Total sale  : " ,total_sale)
    print("Total profit : ",total_sale * 0.2)
    
def display(arr):
    print(arr)
    
def plot(arr):
    ply.scatter([1],arr)
    ply.show()

while(True):
    print("1. Add item")
    print("2. Register Sale")
    print("3. Total sale and profit")
    print("4. Display inventory")
    print("5. Plot")
    x = input("Choose option : ")
    if(x == "1"):
        add_item(arr)
    elif(x == "2"):
        sales(arr, total_sale)
    elif(x == "3"):
        sale_profit(arr, total_sale)
    elif(x == "4"):
        display(arr)
    elif(x == "5"):
        plot(arr)
    else:
        break

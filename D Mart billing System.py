#D-mart Billing system
print("------Welcome to DMart------")
print("Place Your Order Here.")
DM={1:'facewash',2:'handwash',3:'cadbury',4:'toothpest',5:'shampoo',6:'oil'}
price={1:250,2:150,3:100,4:80,5:180,6:120}

items=[]
quantity=[]

while True:
    print(""" Available items:
          1.facewash
          2.handwash
          3.cadbury
          4.toothpest
          5.shampoo
          6.oil  """)
    i=int(input("Enter items: "))
    q=int(input("Enter quantity: "))
    items.append(i)
    quantity.append(q)
    print(items)
    print(quantity)
    c=input("Do you want to continue y/n: ")
    if c=='n':
      print("------Bill------")
      print("-"*105)
      print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}"
              .format('srno','items','quantity','price','amount'))
      print("-"*105)
      sum=0
      for i in range(len(items)):
            print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}"
                  .format(i+1,DM[items[i]],quantity[i],price[items[i]],quantity[i]*price[items[i]]))
            sum=sum+quantity[i]*price[items[i]]
      print("Your Total Bill:",sum)
      gst=sum*9/100
      print("Total GSt: ",gst)
      Total_Bill=sum+gst
      print("Your Total Bill with GSt:",Total_Bill)
      print("Thank You..! Visit Again.Have A Nice Day")

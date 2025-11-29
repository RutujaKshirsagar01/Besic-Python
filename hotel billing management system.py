# Hotel Bill management system project 

db={1:'poha',2:'vadapav',3:'Tea',4:'sandwich',5:'pizza'}
price={1:25,2:20,3:10,4:50,5:100}

items=[]
qu=[]

while True:
    print(""" JDB hotel
          1.poha
          2.vadapav
          3.Tea
          4.sandwich
          5.pizza""")
    i=int(input("Enter items: "))
    q=int(input("Enter quantity: "))
    items.append(i)
    qu.append(q)
    print(items)
    print(qu)
    c=input("Do you want to continue y/n: ")
    if c=='n':
        print("Bill")
        print("-"*105)
        print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format("srno",'items','quantity','price','amount'))
        print("-"*105)
        sum=0
        for i in range(len(items)):
            print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format(i+1,db[items[i]],
                                                              qu[i],price[items[i]],
                                                              qu[i]*price[items[i]]))
            sum=sum+qu[i]*price[items[i]]
    print("Your total bill=",sum)

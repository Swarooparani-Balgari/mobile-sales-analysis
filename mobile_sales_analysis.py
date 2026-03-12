import pandas as pd

data={
    "Sales_Person":['Rahul','Neha','Amit','Priya','Rahul','Neha','Karan','Amit','Priya','Rahul'],
    "City":['Delhi','Mumbai','Bangalore','Delhi','Hyderabad','Mumbai','Bangalore','Delhi','Hyderabad','Delhi'],
    "Brand":['Samsung','Apple','Xiaomi','Apple','Samsung','OnePlus','Xiaomi','Samsung','Apple','OnePlus'],
    "Model":['Galaxy S22','iPhone 14','Redmi Note 12','iPhone 13','Galaxy A54','OnePlus 11','Redmi 12','Galaxy S22','iPhone 14','OnePlus 11'],
    "Quantity":[1,1,2,1,2,1,3,1,1,1],
    "UnitPrice":[72000,80000,18000,65000,30000,62000,15000,72000,80000,62000],
    "Discount":[3000,2000,1000,1500,2000,2500,1200,3000,2000,2000]
    }

df=pd.DataFrame(data)

df["Revenue"]=(df["Quantity"]*df["UnitPrice"])-df["Discount"]
print("Total_Revenue:",df["Revenue"].sum())

print("Revenue by Brand")
print(df.groupby("Brand")["Revenue"].sum().sort_values(ascending=False))

print("\nRevenue by City")
print(df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

print("\nRevenue by Sales_Person")
print(df.groupby("Sales_Person")["Revenue"].sum().sort_values(ascending=False))



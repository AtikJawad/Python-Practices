#shopping cart with Billing program
# Add 15% VAT

products=[]
prices=[]
quantity=[]
total=0

product = input("Enter a Product : ")
price=float(input(f"Enter the price $ of {product} per unit: "))
q=int(input("How Many? :"))
products.append(product)
prices.append(price)
quantity.append(q)
while True:
    product = input("Enter another Product (press 'e' to exit): ")
    if product.lower()=='e':
        break
    else:
        price=float(input(f"Enter the price $ of {product} per unit: "))
        q=int(input("How Many? :"))
        products.append(product)
        prices.append(price)
        quantity.append(q)

for i in range(len(prices)):
    total+=prices[i]*quantity[i]
print(".....Your Cart.....")
print("Product | Quantity | Price (per unit) | Total Price(Quantity x Price)")
for i in range(len(products)):
    print(f"{products[i]}      |     {quantity[i]}       |    {prices[i]:.2f}       |      {(quantity[i]*prices[i]):.2f}")
print("--------------------------------------------------------------------")
print(f"TOTAL AMOUNT (+VAT) to PAY:        {(total+(total*0.15)):.2f} $ only")

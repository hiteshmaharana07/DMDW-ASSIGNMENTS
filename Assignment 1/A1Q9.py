class Product:
    def input(self):
        self.product_no = int(input("Enter the Product Number: "))
        self.product_name = input("Enter the Product Name: ")
        self.cost = float(input("Enter the Cost: "))
        self.quantity = int(input("Enter the Quantity: "))
    def calculate(self):
        self.total_amount = self.cost * self.quantity
    def display(self):
        print("Product Number :", self.product_no)
        print("Product Name   :", self.product_name)
        print("Cost           :", self.cost)
        print("Quantity       :", self.quantity)
        print("Total Amount   :", self.total_amount)
products = []
for i in range(3):
    print("\nEnter Product", i + 1)
    p = Product()
    p.input()
    p.calculate()
    products.append(p)
highest = products[0]
for p in products:
    if p.total_amount > highest.total_amount:
        highest = p
print("\nProduct with Highest Total Amount")
highest.display()

class BMW:
    def __init__(self,price,age,colour):
        self.price = price
        self.age = age
        self.colour = colour
        
class customer:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def customer_info(self):
        print(f"Customer name: {customer.name},Customer gender: {customer.gender},Customer age: {customer.age}")
    
class Ferrari(BMW):
    def __init__(self,price,age,colour):
        super().__init__(self,price,age,colour)
        self.price = price
        self.age = age
        self.colour = colour
        
customer1 = customer("Ryan",14,"Male")
customer2 = customer("Ishan",13"Male")

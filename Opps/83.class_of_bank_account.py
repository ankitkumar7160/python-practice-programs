class Bank_Account():
    
    def __init__(self,account_id,name,account_no,account_type):
        self.account_id = account_id
        self.name = name
        self.account_no = account_no
        self.account_type = account_type
        
    def details_customer(self):
        return f"===Customer Details=== \nAccount_id : {self.account_id}\nName : {self.name}\nAccount No : {self.account_no}\nAccount Type : {self.account_type}\n"
    
customer1 = Bank_Account(101,"Akash",2304324,"Saving")
customer2 = Bank_Account(102,"Ankit",2304327,"Current")

print(customer1.details_customer())
print(customer2.details_customer())
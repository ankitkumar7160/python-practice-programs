
class Bank_Acount:
    
    def __init__(self,id,name,acc_no,acc_type,balance):
        
        self.id = id
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def transfer(self,receiver_user,amount):
        
        if amount <= 0:
            print("Error: Mount must be positive.")
            return False
        
        if self.__balance < amount:
            print(f"Insufficent Balance in Sender Account")
            return False
        
        self.__balance -= amount
        receiver_user.__balance += amount
        print(f"Success: {amount} transfer from {self.name} to {receiver_user.name}")
        
        return f"""
    ===TRANSACTION SUMMARY===
    [SENDER DETAILS]
    Name : {self.name}
    Account No : {self.acc_no}
    Balance : {self.__balance}
    Account Type : {self.acc_type}
    
    [RECEIVER DETAILS]
    Name = {receiver_user.name}
    Account No = {receiver_user.acc_no}
    Balance = {receiver_user.__balance}
    Account Type = {receiver_user.acc_type} """
    
user1 = Bank_Acount(101,"Akash",2304324,"Current",1300)
user2 = Bank_Acount(102,"Ankit",2304325,"Saving",1200)

print(user1.transfer(user2,400))





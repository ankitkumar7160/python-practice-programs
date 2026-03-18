def sum_of_digit(number):
    
    total = 0 
    count = 0
    
    if number == 0:
        return "List is empty."
    
    else :
        temp_number = abs(number)
        while temp_number>0:
            digit = temp_number%10
            total += digit
            
            temp_number//=10
            count +=1
                        
        return total,count
    
number = int(input("Enter the number: "))
sum , count = sum_of_digit(number)

print(f"Sum ({sum}) of this number {number}")
print(f"Count ({count}) of this number {number}")

# print(sum_of_digit(5374))
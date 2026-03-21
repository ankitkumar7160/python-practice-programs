def second_largest_number(my_array):
    # Step 1: Initialize both with the smallest possible value (Negative Infinity)
    # Taaki ye negative numbers wale array ke saath bhi sahi kaam kare.
    largest = float("-inf")
    second_largest = float("-inf")
    
    # Step 2: Array ke har number ko ek-ek karke check karo
    for num in my_array:
        # Case A: Agar naya number 'largest' se bhi bada nikalta hai
        if num > largest:
            # Puraana 'largest' ab promotion kho kar 'second_largest' ban jayega
            second_largest = largest
            # Naya number 'largest' ki kursi par baith jayega
            largest = num
            
        # Case B: Agar naya number 'largest' se bada nahi hai, par 'second_largest' se bada hai
        # (Saath hi ye check karna zaroori hai ki naya number 'largest' ke barabar na ho)
        elif num > second_largest and num != largest:
            # Sirf 'second_largest' ko update karo
            second_largest = num
    
    return second_largest

# --- Execution ---
my_array = input("Enter values of array (space separated): ")
new_array = [int(x) for x in my_array.split()]

result = second_largest_number(new_array)

# Agar array mein second largest mila hi nahi (e.g. [10, 10, 10])
if result == float("-inf"):
    print("There is no second largest number.")
else:
    print(f"Second largest of this array: {result}")
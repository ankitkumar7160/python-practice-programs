# # User se array ki length (kitne numbers honge) input lena
# n = int(input("Enter the length of array: "))

# # Khali list (array) create karna values store karne ke liye
# array = []

# # Loop chala kar user se 'n' baar values lena aur array mein add karna
# for i in range(n):
#     val = int(input("Enter the values: "))
#     array.append(val)

# print(f"Your original array {array}")

# # Edge case check: Agar array khali ho toh aage ka process na chale
# if len(array) == 0:
#     print("The array is empty.")
# else:
#     # --- BUBBLE SORT LOGIC STARTS HERE ---
    
#     # Outer Loop: Ye loop 'n' baar chalega taaki har number apni sahi jagah pahunch sake
#     for x in range(n):
        
#         # Inner Loop: Ye padosi (adjacent) numbers ko compare karta hai
#         # 'n-x-1' ka matlab hai ki sorted numbers ko dobara check nahi karna
#         for j in range(0, n - x - 1):
            
#             # Condition: Agar left side wala number right side wale se bada hai
#             if array[j] > array[j+1]:
                
#                 # Swapping Logic: Do numbers ki jagah aapas mein badalna
#                 temp = array[j]       # Left value ko temp mein surakshit (save) rakha
#                 array[j] = array[j+1] # Right value ko left position par move kiya
#                 array[j+1] = temp     # Temp se purani left value ko right position par dala

# # Final sorted array ko print karna
# print(f"Sorted array {array}")




n = int(input("Enter the elngth of array: "))

array = []

for i in range(n):
    i = int(input("Enter the values: "))
    array.append(i)

print(f"Original array {array}")

if len(array) == 0:
    print("The array is empty.")
else:
    
    for x in range(n):
        main_index = x
        for j in range(x+1,n):
            
            if array[j] < array[main_index]:
                main_index = j
        array[x], array[main_index] = array[main_index], array[x]
        
print(f"Sorted array {array}")
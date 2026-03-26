# def remove_duplicate_element(my_array):
    
#     uniqe_set = {}
    
#     duplicate_list = list(my_array)
    
#     for num in my_array:
#         if num in uniqe_set:
#             if num in duplicate_list:
#                 duplicate_list.remove(num)
        
#         else:
#             uniqe_set[num] = True
            
    
#     return duplicate_list

# my_array =  input("Enter arrays Values: ")
# new_array = [int(x) for x in my_array.split()]

# result = remove_duplicate_element(new_array)

# print(result)





def remove_duplicate_element(my_array):
    
    uniqe_set = {}
    
    duplicate_list = []
    
    for num in my_array:
        if num not in uniqe_set:
            duplicate_list.append(num)
            uniqe_set[num] = True
        
    
    return duplicate_list

my_array =  input("Enter arrays Values: ")
new_array = [int(x) for x in my_array.split()]

result = remove_duplicate_element(new_array)

print(result)
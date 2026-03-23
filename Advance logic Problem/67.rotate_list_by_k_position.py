def rotate_list(my_array, k):
    
    n = len(my_array)
    
    k = k % n
    
    rotate_list = []
    
    if k == 0:
        return my_array
    
    else:
        part1 = my_array[n-k:]
        part2 = my_array[:n-k]
        
        r_list = part1 + part2
        
        rotate_list.append(r_list)
        
    return rotate_list

my_array = input("Enter values of array seperable by space: ")

k = int(input("Enter value of k: "))

new_array = [int(x) for x in my_array.split()]

result = rotate_list(new_array,k)

print(result)

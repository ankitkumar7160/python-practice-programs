word = input("Enter the string: ")
reversed_string = list(word)
left = 0
right = len(reversed_string)-1

while left < right:
    temp = reversed_string[left]
    reversed_string[left] = reversed_string[right]
    reversed_string[right] = temp
    
    left += 1
    right -= 1

reversed = "".join(reversed_string)
print(f"Original Word {word}")
print(f"Reversed word {reversed}")

if reversed == word:
    print("palind")
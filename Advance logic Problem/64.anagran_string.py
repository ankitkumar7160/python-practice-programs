def isAnagram(string1,string2):
    
    if len(string1) != len(string2):
        return False
    
    count_char = {}
    
    for i in range(len(string1)):
        char1 = string1[i]
        count_char[char1] = count_char.get(char1,0)+1
        
        char2 = string2[i]
        count_char[char2] = count_char.get(char2,0)-1
       
       
    for count in count_char.values():
        if count != 0:
            return False
        
    return True

string1 = "Silent".lower()
string2 = "Lisent".lower()

result = isAnagram(string1, string2)

print(f"Strings are Anagram {result}")
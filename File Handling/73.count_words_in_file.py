def count_word():
    
    with open ("File Handling/Note.txt" , "r") as file:
        
        content = file.read()
        
    file.close()
    
    words = content.split()
    # count_word = []
    # # count = 0
    # for word in words:
    #     # count += 1
    #     count_word.append(word)
        
    return len(words)

print(count_word())
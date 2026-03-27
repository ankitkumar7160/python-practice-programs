def count_word():
    # 1. READ ACCESS: 'with' ensures the file is closed automatically.
    # Logic: It creates a temporary bridge between your RAM and the Hard Drive.
    with open ("File Handling/Note.txt" , "r") as file:
        
        # 2. SLURPING: read() pulls the entire file into a single String variable.
        # Logic: All text, spaces, and newlines are now one "blob" in memory.
        content = file.read()
        
    # Mentor Note: 'file.close()' is not needed here; 'with' already did it!
    # Once we are here, the file is safely unlinked from the program.

    # 3. TOKENIZATION: split() breaks the string into pieces.
    # Logic: It uses "Whitespace" (spaces, tabs, newlines) as a knife.
    # Result: "Hello World\nHow are you" -> ["Hello", "World", "How", "are", "you"]
    words = content.split()
    
    # --- Manual Accumulation (Commented Out) ---
    # count_word = []
    # for word in words:
    #     count_word.append(word)
    # Logic: This "Bucket Brigade" logic is redundant because 'words' 
    # is already the exact list we need.
        
    # 4. MEASUREMENT: len() provides the count of items in the list.
    # Logic: Instead of counting 1, 2, 3... we look at the list's metadata.
    return len(words)

# 5. EXECUTION: Prints the final integer result to the console.
print(count_word())
def count_lines():
    # 1. ESTABLISH ACCESS: 'with' creates a managed environment.
    # Logic: It asks the OS for a "Read" handle. Once the code exits this 
    # indented block, the file is automatically closed (Safety first!).
    with open ("File Handling/Note.txt" , "r") as file:
        
        # 2. DATA INGESTION: readlines() scans for the '\n' (newline) character.
        # Logic: It pulls the entire file into RAM and slices it into a List.
        lines = file.readlines()
        
        # Mentor Note: file.close() is actually redundant here because 'with' 
        # already handles the closing logic for you.
        file.close() 
        
    # 3. QUANTIFICATION (The "For Loop" vs "Len" Logic):
    
    # --- Manual Counter Logic ---
    # count = 0
    # for line in lines:
    #     count += 1
    # Logic: This is "Linear Scan" logic. It looks at every item individually.
    # Use this ONLY if you need to inspect lines (e.g., "ignore empty lines").
        
    # --- Optimized Logic ---
    # Logic: len() is a "Constant Time" operation. Since 'lines' is already 
    # a list, the computer simply checks the list's metadata for its size.
    return len(lines)
        
# 4. EXECUTION: Calls the logic and prints the final integer result.
print(count_lines())
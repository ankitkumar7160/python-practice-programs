# file = open("Notes.txt" , "w")
# file.write(input("Enter Notes: "))
# file.close


print("Write your note in NOtes file.")
def create_file(new_file):
    file = open("Note.txt" , "w")
    file.write(new_file)
    file.close()
    
    return file

new_file = input("enter data: ")
print(create_file(new_file))
print("Sessuccesfully Write in the file.")
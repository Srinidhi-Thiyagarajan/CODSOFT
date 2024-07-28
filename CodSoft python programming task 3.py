import string
import random
 
length_of_password = int(input("Enter password length: "))
 
print('''\nSelect the type of password : \n
         1. Digits\n
         2. Letters\n
         3. Special characters\n
         4. Exit\n''')
 
char_list = ""
 
while(True):
    option = int(input("\nSelect a number :  "))
    if(option == 1):
          char_list += string.ascii_letters
    elif(option == 2):
         char_list += string.digits
    elif(option == 3):
         char_list += string.punctuation
    elif(option == 4):
        break
    else:
        print("\nPlease select a valid option ! ")
 
password = []
 
for i in range(length_of_password):
   random_char = random.choice(char_list)
   password.append(random_char)
print("\nYour password has been generated.")
print("\nThe random password is " + "".join(password))

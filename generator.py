import random

def generator_password(password_length):
    uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    downcase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    number = [1,2,3,4,5,6,7,8,9,0]
    symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_"]
    password_length = password_length
    password = ""

    for x in range(password_length):
        junk_password = random.randrange(1,5)
        if junk_password == 1:
            password += uppercase[random.randrange(1,26)]
        elif junk_password == 2:
            password += downcase[random.randrange(1,26)]
        elif junk_password == 3:
            password += str(number[random.randrange(1,10)])
        elif junk_password == 4:
            password += symbol[random.randrange(1,10)]
    
    print(f"Password: {password}")

password_length = int(input("Password length: "))
repeat = int(input("Number of passwords: "))
for x in range(repeat):
    generator_password(password_length)
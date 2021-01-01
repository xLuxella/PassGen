import random, string
length = int(input("How many characters should your password be? "))
char = string.ascii_letters + string.digits + string.punctuation
password = []
for x in range(length):
    password.append(random.choice(char))
print(''.join(password))


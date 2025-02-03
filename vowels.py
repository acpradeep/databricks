my_string = input("Please enter your name: ")

count = 0

vowels = ["a","e","i","o","u"]

for char in my_string:
    if char in vowels:
        count+=1
    else:
        pass
print(f"{my_string} has {count} vowels. ")
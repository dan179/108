
# I'm a comment, not code 


# variables
name = "daniel"
last = "chavez"
age = 99
found = False
price = 19.99


print(name + " " + last)



print(age + 1)
print(age * 1)
print("Hi I'm " + name + ", and my age is: " + str(age))

print(f"Hi I'm {name}, and my age is: {age}")



if age < 100:
    print("Don't worry, you are still young")
    print("I'm inside the if")
    print("me too")

elif age == 100: 
    print("Congrats you got to a century!!!")

else:
    print("Sorry, you are getting old!!!!")




print("I'm not :(")





def say_hello():
    print("Hello from a fn")
    print("I'm inside the fn")



say_hello()
say_hello()
say_hello()
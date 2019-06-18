name = "John Waston"
print(len(name))            #11

print(max(name))            # t
print(min(name))            #space

print(name[1])              #o
print(name[len(name)-1])    #n

print(name[-1])             #n
print(name[1:3])            # oh

print(name + "California")
print(name)                 #Concatenation will not modify old string

email = "john@example.com"
password = "pass123"

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Not Valid Email")

if len(password) > 6:
    print("A Valid Password Length")
else:
    print("Not Valid Password Length")
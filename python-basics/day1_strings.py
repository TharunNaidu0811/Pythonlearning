message = 'hello world'
message_1 = "it's my first project"
message_2 = """This is my first
python code"""
test1 = "tharun"
test2 = "naidu"
#length of the string
print(len(message))
#reverse string
print(message[::-1])
#slicing 
print(message[0:5])
print(message[0:])
print(message[:5])

# Count 
print(message.count('o'))
print(message.count('world'))

# find 
print(message.find("w"))
#replace
message_3 = message_1.replace('first','second')
print(message_3)

#lower & upper 
print(test1.lower())
print(test1.upper())

#concate
print(test1 + " "+test2)

#String formatting (f formating)
print(f"First name  : {test1}")
print(f"Second name : {test2}")

#title()
tittle1 = "mahesh"
print(tittle1.title())

#strip 
strip1 = "  Tharun Naidu Routhu  "
print(strip1.strip())

#slice, startswith, endswith,  in 
step1 = "Tharun Naidu Routhu"
print(step1.split())
print(step1.startswith("Tha"))
print(step1.endswith("thu"))
print("Tharun" in step1)

#capitilize
cap = "rowdy rathode"
print(cap.capitalize())




print(message)
print(message_1)
print(message_2)

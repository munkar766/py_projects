z = input("Greeting: ")

z = z.lower()
z = z.replace(" ", "")

if "hello" in z:
    print("$0")
elif z.find("h") == 0 and z!= "hello":
    print("$20")
else:
    print("$100")

print("Welcome to Aahana Bell! This is your food ordering chatbot")
name=input("What is your name? ")
age=input("Hello "+name+", how old are you? ")
print("Welcome again to Aahana Bell "+name+ "! How can I help a young "+age+ " year old like you today?" )
print("")
print("Please choose from the following options by entering 1,2,3,4:") 
print("1: Option 1\n2: Option 2\n3: Option 3\n4. Exit ")
choice=input("What is your choice?")

if choice=="4":
    print("Goodbye "+name+" come to Aahana Bell anytime!")
elif choice=="3":
    print("Option 3")
elif choice=="2":
    print("Option 2")
elif choice=="1":
    print("Option 1")


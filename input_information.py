print("Please provide necessary information")

profile = {}

#Loop1: Asks the user to input their information
while True:
    
    #Loop2: Allows the user to auto-retry if input is invalid
    while True:
        try:
            name = input("Name: ")
            age = int(input("Age: "))

            #Store each profile input in a dictionary
            profile[name] = age
            
            print(f"{name}")
            print(f"{age}")

            retry = input("Do you want to make any changes? (Yes/No) ")
            
            #Stops Loop2
            break
        
        except:
            print("Please input valid name or age.")
    
    if retry == "Yes":
        print("Please provide your information.")
    
    #Stops Loop1
    elif retry == "No":
        print(f"The oldest is {name} with age {age}.")
        break
    

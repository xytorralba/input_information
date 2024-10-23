print("Please provide your")

Profile = {}

#Loop1: Asks the user to input their information
while True:
    
    #Loop2: Allows the user to auto-retry if input is invalid
    while True:
        try:
            name = input("Name: ")
            age = int(input("Age: "))

            Profile = {
                "name" : name,
                "age" : age
            }

            print(Profile["name"])
            print(Profile["age"])

            #Store each profile input in a dictionary
            Profile[name] = age
            
            retry = input("Do you want to make any changes? ")
            #Stops Loop2
            break
        except:
            print("Please input valid name or age.")
    
    if retry == "Yes":
        print("Please provide your information.")
    
    #Stops Loop1
    elif retry == "No":
        print(Profile["name"])
        print(Profile["age"])
        break
    

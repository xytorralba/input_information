Profile = {}

#Loop1: Asks the user to input their information
while True:
    try:
        name = print(input("Name: "))
        age = print(int(input("Age: ")))

        Profile = {
            "name" : name,
            "age" : age
        }

        print(Profile["name"])
        print(Profile["age"])
        
        #Stops Loop1
        break
    except:
        print("Please input valid name or age.")

#Loop2: Allows the user to auto-retry if input is invalid

#Stops Loop2
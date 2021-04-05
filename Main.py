from src.Scraper import URLInstance, ShowMenu, CheckConnection

# Checking the Internet Connection on Startup
print("Checking Internet Connection..")
CheckConnection()

name = input("Enter the Name of the Service: ")
# Creating the Instance
instance = URLInstance(name)

# Checking is the entered string is blank
if not name:
    print("Blank Name!")
    quit()
else:
    pass

# Showing the Menu and Processing the Input
ShowMenu()

while True:

    option = int(input("Enter the Option Number: "))
    if option == 1:
        instance.GetStatus()
    elif option == 2:
        instance.OpenURL()
    elif option == 3:
        instance.GetURL()
    elif option == 4:
        instance.GetBaseURL()
    elif option == 5:
        name = input("Enter the Name of the Service: ")
        # Overwriting the Previous Instance Object
        instance = URLInstance(name)
        ShowMenu()
    elif option == 6:
        print("Thanks for Using!")
        quit()
    else:
        print("Please Enter Valid Value!")

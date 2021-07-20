from src.Scraper import URLInstance, menu, check_connection

# Checking the Internet Connection on Startup
print("Checking Internet Connection..")
check_connection()

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
menu()

while True:

    option = int(input("Enter the Option Number: "))
    if option == 1:
        instance.get_status()
    elif option == 2:
        instance.open_url()
    elif option == 3:
        instance.get_url()
    elif option == 4:
        instance.get_base_url()
    elif option == 5:
        name = input("Enter the Name of the Service: ")
        # Overwriting the Previous Instance Object
        instance = URLInstance(name)
        menu()
    elif option == 6:
        print("Thanks for Using!")
        quit()
    else:
        print("Please Enter Valid Value!")

import Read
import Write
import datetime
import Operation

def RentingLand():
    invoices_details = []
    while True:
        try:
            LandDetails = Read.read_LandDetails()  # read land details
            available_LandDetails = [land for land in LandDetails if land['Status'] == "Available"]  # Filter available lands
            
            if available_LandDetails:
                print("Available lands are:")
                print("_" * 153)
                
                print("KittaNum   |   City   |   Direction   |   Anna   |   Cost   |   Status")
                print("_" * 153)
                for land in available_LandDetails:
                    print(land['KittaNum'], " " * (12 - len(str(land['KittaNum']))),
                          land['City'], " " * (12 - len(land['City'])),
                          land['Direction'], " " * (12 - len(land['Direction'])),
                          land['Anna'], " " * (9- len(str(land['Anna']))),
                          land['Cost'], " " * (9 - len(str(land['Cost']))),
                          land['Status'])
                print("_" * 153)

                KittaNum = int(input("Enter the kitta number of the land you want to rent: "))
                if KittaNum not in [land['KittaNum'] for land in available_LandDetails]:
                    print("Land with kitta number", KittaNum, "is not available for rent.")
                    continue

                land = next(land for land in available_LandDetails if land['KittaNum'] == KittaNum)


                selected_Anna = int(input("Enter the selected Anna (size) of the land: "))
                if selected_Anna != land['Anna']:
                    print("You must rent the entire plot of land. Partial renting is not allowed.")
                    continue
                
                Name = input("Please insert your name:  ")
                while not Name.isalpha() or Name.isspace():
                    print("Enter a name (Only alphabets and spaces are allowed.)")
                    Name = input("Insert your name:  ")

                Address = input("Please store your address: ")
                while not Address.replace(" ", "").isalpha():
                    print("Please enter a valid address.")
                    Address = input("Store your address: ")

                Phonenumber = input("Please input your phone number: ")
                while not Phonenumber.isdigit() or len(Phonenumber) != 10:
                    print("Please enter a valid phone number.")
                    Phonenumber = input("Input your phone number: ")

                
                
                

                total_Cost = Operation.calculate_landCost(land["Cost"], selected_Anna)

                while True:
                    Duration = input("Enter your duration (in months): ")
                    if not Duration.isdigit():
                        print("Please enter a valid duration.")
                    else:
                        break

                Current_Datetime = datetime.datetime.now()
                invoice_details = Write.Renting_invoice(Name, Phonenumber, Address, KittaNum, land, land["Cost"], selected_Anna, total_Cost, Duration, Current_Datetime)

                invoices_details.append(invoice_details)

                # Changing the land status to unavailable 
                Write.Update_landStatus(LandDetails, [KittaNum], new_Status='Unavailable')
                print("Land rented successfully!")
                choice = input("Do you want to rent more land? (yes/no): ").lower()
                if choice != 'yes':
                    break
            else:
                print("No lands are currently available for rent.")
                break
        except ValueError:
            print("Invalid input. Enter a valid value.")
            continue

    all_invoices_details = "\n\n".join(invoices_details)

    try:
        Unique_filename = input("Enter file name to save rent invoice: ")
        file_name = Unique_filename + ".txt" 
        with open(file_name, 'w') as file:
            file.write(all_invoices_details)
        print("Invoices are saved in file:", file_name)
    except IOError:
        print("Error: Unable to save the invoices to file.")

def ReturningLand():
    invoices_details = []
    while True:
        try:
            LandDetails = Read.read_LandDetails()  # read land details
            Unavailable_LandDetails = [land for land in LandDetails if land['Status'] == "Unavailable"]  # Filter unavailable lands
            
            if Unavailable_LandDetails:
                print("Unavailable lands are:")
                print("_" * 153)
                print("KittaNum   |   City   |   Direction   |   Anna   |   Cost   |   Status")
                print("_" * 153)
                for land in Unavailable_LandDetails:
                    print(land['KittaNum'], " " * (12 - len(str(land['KittaNum']))),
                          land['City'], " " * (12 - len(land['City'])),
                          land['Direction'], " " * (12 - len(land['Direction'])),
                          land['Anna'], " " * (9 - len(str(land['Anna']))),
                          land['Cost'], " " * (9 - len(str(land['Cost']))),
                          land['Status'])
                print("_" * 153)

                KittaNum = int(input("Enter the kitta number you want to return: "))
                if KittaNum not in [land['KittaNum'] for land in Unavailable_LandDetails]:
                    print("Land with kitta number", KittaNum, "is not available for return.")
                    continue

                
                
                Name = input("Please insert your name:  ")
                while not Name.isalpha() or Name.isspace():
                    print("Enter a name (Only alphabets and spaces are allowed.)")
                    Name = input("Insert your name:  ")
                    

                Address = input("Please store your address:  ")
                while not Address.replace(" ", "").isalpha():
                    print("Please enter a valid address.")
                    Address = input("Store your address:  ")
                    

                Phonenumber = input("Please input your phone number: ")
                while not Phonenumber.isdigit() or len(Phonenumber) != 10:
                    print("Please enter a valid phone number.")
                    Phonenumber = input("Input your phone number: ")

                

                selected_land = None
                for land in Unavailable_LandDetails:
                    if land['KittaNum'] == KittaNum:
                        selected_land = land
                        break

                if not selected_land:
                    print("Land with kitta number", KittaNum, "is not available for return.")
                    continue

                Rental_months = int(input("Enter the number of months the land was rented for: "))
                
                total_Cost = Operation.calculate_landCost(selected_land["Cost"], selected_land['Anna'])

                Returned_months = int(input("Enter the number of months the land was returned after: "))

                fine = Operation.calculate_fine(total_Cost, Rental_months, Returned_months)

                Current_Datetime = datetime.datetime.now()
                
                invoice_details = Write.Returning_invoice(Name, Phonenumber, Address, selected_land, total_Cost, Current_Datetime, Rental_months, Returned_months, fine)

                invoices_details.append(invoice_details)

                # Re-read LandData after each return for consistency
                Write.Update_landStatus(LandDetails, [KittaNum], new_Status='Available')
                print("Land returned successfully!")

                choice = input("Do you want to return more lands? (yes/no): ").lower()
                if choice != 'yes':
                    break
            else:
                print("No lands are currently available for return.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid value.")

    # Combine invoice content and save to a file
    all_invoices_details = "\n\n".join(invoices_details)

    try:
        Unique_filename = input("Enter filename to save the return invoice: ")
        file_name = Unique_filename + ".txt"
        with open(file_name, 'w') as file:
            file.write(all_invoices_details)
        print("Invoices are saved in file:", file_name)
    except IOError:
        print("Error: Unable to save the invoices to file.")

                

def Welcome():
    print("_"*153)
    print("                                              Welcome to techno property nepal portal.")
    print("                                 Techno Property Nepal is a leading land rent and return company in Nepal.")
    print("                           We specialize in renting excellent land and ensuring a hassle-free land return procedure.")
    print("_"*153)
    
    print("Contact us:")
    print("             " )
    print("Address: kumarihall,ktm,Nepal")
    print("Email: contact@Technopropertynepal.com")
    print("phone: +977-0987664455")
    print("Thank you for choosing Techno Property Nepal!")
    print("_"*153)
    print("_"*153)

def lands():
    LandDetails = Read.read_LandDetails()
    print("Lands are:")
    print("_"*153)
    print("KittaNum   |   City   |   Direction   |   Anna   |   Cost   |   Status")
    print("_"*153)
    for land in LandDetails:
        print(land['KittaNum'], " "*(12-len(str(land['KittaNum']))),
              land['City'], " "*(12-len(land['City'])),
              land['Direction'], " "*(12-len(land['Direction'])),
              land['Anna'], " "*(9-len(str(land['Anna']))),
              land['Cost'], " "*(9-len(str(land['Cost']))),
              land['Status'])

Welcome()
lands()

while True:
    print("_"*153)
    print("1. Rent a land")
    print("2. Return a land")
    print("3. Exit")
    print("_"*153)

    choice = input("Choose one of these numbers: ")

    if choice == '1':
        RentingLand()
    elif choice == '2':
        ReturningLand()
    elif choice == '3':
        print("                                 Thank you for using Techno Property Nepal Portal.Hope you will visit next time!")
        break
    else:
        print("   Invalid choice! Please enter a number between 1,2 and 3.")

    

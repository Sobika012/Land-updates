import Operation
import datetime

def Renting_invoice(Name, Phonenumber, Address,KittaNum, land, Cost, selected_Anna, total_Cost, Duration, Current_Datetime):
    invoice_details = "\nInvoice:\n"
    invoice_details += "     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    invoice_details += "     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome to Techno Property Nepal Portal~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    invoice_details += "     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"


    
    invoice_details +="Invoice Date: " + Current_Datetime.strftime("%Y-%m-%d %H:%M:%S") + "\n" "\n"
    invoice_details +="Name: " + Name + "\n"
    invoice_details +="Phonenumber: "+ Phonenumber + "\n"
    invoice_details +="Address: "+ Address + "\n"
    invoice_details +="KittaNum: " + str(land["KittaNum"])+ "\n"
    invoice_details +="Selected Land: \n"
    invoice_details +="City: " + land["City"] + "\n"
    invoice_details +="Direction: " + land["Direction"] + "\n"
    invoice_details +="Selected Anna: " + str(selected_Anna) + "\n"
    invoice_details +="Cost: NPR " + str(Cost) + "\n"
    invoice_details += "Total Cost: NPR " + str(total_Cost) + "\n" 
    invoice_details += "Rental Duration: " + str(Duration) + " months\n"  # Convert duration to string
 
    return invoice_details

def Update_Status(file_name, LandDetails):
    """
    Updates the status of lands in the text file.
    """
    with open(file_name, 'w') as file:
        for land in LandDetails:
            land_data = (
                str(land['KittaNum']) + " " + 
                str(land['City']) + " " + 
                str(land['Direction']) + " " + 
                str(land['Anna']) + " " + 
                str(land['Cost']) + " " + 
                str(land['Status']) + "\n"
            )
            file.write(land_data)

def Update_landStatus(LandDetails, KittaNum, new_Status):#Updates the status of specified lands.
    
    for land in LandDetails:
        if land['KittaNum'] in KittaNum:
            land['Status'] = new_Status
    Update_Status('LandDetails.txt', LandDetails)

def Returning_invoice(Name, Phonenumber, Address, land, total_Cost, Current_Datetime, Rental_months, Returned_months, fine):
    invoice_details = "\nInvoice:\n"
    invoice_details += "     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    invoice_details += "     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome to Techno Property Nepal Portal~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    invoice_details += "     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"


    
    invoice_details += "Invoice Date: " + Current_Datetime.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    invoice_details += "Name: " + Name + "\n"
    invoice_details += "Phonenumber: " + Phonenumber + "\n"
    invoice_details += "Address: " + Address + "\n"
    invoice_details += "KittaNum: " + str(land["KittaNum"]) + "\n"
    invoice_details += "Rental Duration: " + str(Rental_months) + " months\n"
    invoice_details += "Returned After: " + str(Returned_months) + " months\n"
    invoice_details += "Total Cost: NPR " + str(total_Cost) + "\n"
    invoice_details += "Fine: NPR " + str(fine) + "\n"
    invoice_details += "Total Amount Due: NPR " + str(total_Cost + fine) + "\n"

    return invoice_details

    

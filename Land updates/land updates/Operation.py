def calculate_landCost(Cost, selected_Anna):#calculate garney price
   
    total_Cost = Cost * selected_Anna
    return total_Cost

        

def calculate_fine(total_Cost, Rental_months, Returned_months):
    if Returned_months <= Rental_months:
        return 0  # No fine if returned on time or earlier
    else:
        Extra_months = Returned_months - Rental_months
        fine = 0.1 * total_Cost * Extra_months
        return fine

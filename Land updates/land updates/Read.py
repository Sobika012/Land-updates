def read_LandDetails():
    """Reads land data from 'LandDetails.txt' and returns a list of dictionaries."""
    LandDetails = []
    try:
        with open('LandDetails.txt', 'r') as file:  # r = read only
            for line in file:
                # Split line into data elements (assuming whitespace separated)
                data = line.split()

                if len(data) >= 6:  # Ensure 6 columns
                    KittaNum = int(data[0])
                    City = data[1]
                    Direction = data[2]
                    Anna = int(data[3])
                    Cost = int(data[4])
                    Status = data[5]

                    # Create a dictionary for each land entry
                    land_data = {
                        'KittaNum': KittaNum,
                        'City': City,
                        'Direction': Direction,
                        'Anna': Anna,
                        'Cost': Cost,
                        'Status': Status
                    }
                    LandDetails.append(land_data)
    except FileNotFoundError:
        print("ERROR: Data is not found.")
    return LandDetails


def find_landBy_Kitta(KittaNum):
    """Searches land with KittaNumber and returns it with details."""
    LandDetails = read_LandDetails()  # Get all land data from the file
    for land in LandDetails:
        if land['KittaNum'] == KittaNum:
            return land  # If kitta number matches, return land
    return None  # If no matching land is found, return None

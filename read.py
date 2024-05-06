def read_file():
    # Open the file
    file = open("land.txt", "r")
    
    # Create an empty list to store land data
    lands = []

    # Read each line in the file
    for each in file:
    # Remove newline character at the end of the line and split by comma
        line_data = each.replace("\n", "").split(',')

        
        # Create a dictionary for each land
        land = {
            "kitta_number": line_data[0],
            "city_district": line_data[1],
            "land_faced": line_data[2],
            "area": line_data[3],
            "price": line_data[4],
            "status": line_data[5]
        }

        # Add the land dictionary to the list
        lands.append(land)
    
    # Close the file
    file.close()
    
    # Return the list of land dictionaries
    return lands


'''# Call the function to read the file
land_data = read_file()

# Print the land data
for land in land_data:
    print(land)'''

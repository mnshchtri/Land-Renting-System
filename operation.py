from write import write_to_file, write_return_invoice
def rent_land(lands):
    # Function to rent a land
    kitta_number = input("Dear User, Please enter the kitta number of the land you want to rent: ")
    for land in lands:
        if land["kitta_number"] == kitta_number:
            if land["status"] == "Available":
                customer_name = input("Enter your name: ")
                rent_duration = int(input("Enter the duration of rent (in months): "))
                total_amount = int(land["price"]) * rent_duration
                land["status"] = "Not Available"
                # Call write_to_file function
                write_to_file(land, customer_name, rent_duration, total_amount)
                return land, customer_name, rent_duration, total_amount
            else:
                print("This land is not available for rent.")
                return 
    print("Land not found.")
    return 

def return_land(lands):
    # Function to return a land
    kitta_number = input("Enter the kitta number of the land you want to return: ")
    for land in lands:
        if land["kitta_number"] == kitta_number:
            if land["status"] == "Not Available":
                # Update status to "Available"
                land["status"] = "Available"
                # Call write_return_invoice function
                write_return_invoice(land)
                return land
            else:
                print("This land is already available.")
                return 
    print("Land not found.")
    return 

    
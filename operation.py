from write import write_to_rent_invoice, write_to_return_invoice
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
                #generate invoice in terminal
                print("\n**************************************************************************************\n")
                print("\nYour Invoice has been generated.")
                print("\n==============================Techno Property Nepal===================================")
                print("                              Kamal Pokhari, Kathmandu                                  ")
                print("======================================================================================")
                print("Invoice of your rented land: \n")
                print("Customer Name: " + customer_name + "\n")
                print("Kitta Number: " + land['kitta_number'] + "\n")
                print("City/District: " + land['city_district'] + "\n")
                print("Land Faced: " + land['land_faced'] + "\n")
                print("Duration of rent: " +str(rent_duration) + " months\n")
                print("Total Amount: " + str(total_amount) + "\n")
                print("--------------------------------------------------------------------------------------\n")
                # Update status in lands.txt
                with open("land.txt", "w") as lands_file:
                    for l in lands:
                        if l["kitta_number"] == kitta_number:
                            l["status"] = "Not Available"
                        lands_file.write(",".join([l["kitta_number"], l["city_district"], l["land_faced"], l["area"], l["price"], l["status"]]) + "\n")
                
                # Call write_to_file function
                write_to_rent_invoice(land, customer_name, rent_duration, total_amount)
                return land, customer_name, rent_duration, total_amount
            else:
                print("This land is not available for rent.")
                return 
    print("Land not found.")
    return 

def return_land(lands, rent_duration):
    while True:
        # Function to return a land
        kitta_number = input("Enter the kitta number of the land you want to return: ")
        for land in lands:
            if land["kitta_number"] == kitta_number:
                if land["status"] == "Not Available":
                    customer_name = input("Enter your name: ")
                    returned_duration = int(input("Enter the duration of returned (in months): "))
                    price_per_month = int(land["price"])
                    total_amount = 0
                    if returned_duration > rent_duration:
                        # Calculate the total amount with fine
                        delayed_months = returned_duration - rent_duration
                        fine_price = 0.1 * delayed_months * price_per_month
                        total_amount = (returned_duration * price_per_month) + fine_price
                        print("\nYou returned the land after the rented months. A fine of 10% of the total amount has been applied.")
                    
                    elif returned_duration <= rent_duration:
                        # Calculate the total amount without fine
                        total_amount = returned_duration * price_per_month
                        print("\nYou returned the land before or within the rented months. No fine applied.")
    
    
                    # Update status to "Available"
                    land["status"] = "Available"
                    '''generate invoice in

                        terminal'''
                    print("\n**************************************************************************************\n")
                    print("\nYour Invoice has been generated.")
                    print("\n==============================Techno Property Nepal===================================")
                    print("                              Kamal Pokhari, Kathmandu                                  ")
                    print("======================================================================================")
                    print("Invoice of your returned land: \n")
                    print("Customer Name: " + customer_name + "\n")
                    print("Kitta Number: " + land['kitta_number'] + "\n")
                    print("City/District: " + land['city_district'] + "\n")
                    print("Land Faced: " + land['land_faced'] + "\n")
                    print("Duration of returned: " + str(returned_duration) + " months\n")
                    print("Total Amount: " + str(total_amount) + "\n")
                    print("--------------------------------------------------------------------------------------\n")
                    
                    # Update status in lands.txt
                    with open("land.txt", "w") as lands_file:
                        for l in lands:
                            if l["kitta_number"] == kitta_number:
                                l["status"] = "Available"
                            lands_file.write(",".join([l["kitta_number"], l["city_district"], l["land_faced"], l["area"], l["price"], l["status"]]) + "\n")
                    
                    # Call write_return_invoice function
                    write_to_return_invoice(land, customer_name, returned_duration, total_amount)
                    return land, customer_name, returned_duration, total_amount
                else:
                    print("This land is already available.")
                    return 
        print("Land not found.")
        return



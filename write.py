def write_to_file(land, customer_name, rent_duration, total_amount):
    # Open a file to write the invoice
    with open("rent_invoice_" + land['kitta_number'] + ".txt", "w") as invoice_file:
        # Write the invoice details
        invoice_file.write("--------------------------------Techno Property Nepal---------------------------------")
        invoice_file.write("                               Kamal Pokhari, Kathmandu                               ")
        invoice_file.write("--------------------------------------------------------------------------------------")
        invoice_file.write("Invoice of your rented land: ")
        invoice_file.write("Customer Name: " + customer_name + "\n")
        invoice_file.write("Kitta Number: " + land['kitta_number'] + "\n")
        invoice_file.write("City/District: " + land['city_district'] + "\n")
        invoice_file.write("Land Faced: " + land['land_faced'] + "\n")
        invoice_file.write("Area: " + land['area'] + " anna\n")
        invoice_file.write("Date and Time of Rent: <datetime>\n")
        invoice_file.write("Duration of Rent: " + str(rent_duration) + " months\n")
        invoice_file.write("Total Amount: " + str(total_amount) + "\n")
    # Confirm successful invoice generation
    print("Success: Land rented. Invoice generated.")

def write_return_invoice(land):
    # Open a file to write the return invoice
    with open("return_invoice_" + land['kitta_number'] + ".txt", "w") as invoice_file:
        # Write the return invoice details
        invoice_file.write("--------------------------------Techno Property Nepal---------------------------------")
        invoice_file.write("                               Kamal Pokhari, Kathmandu                               ")
        invoice_file.write("Invoice of your rented land:\n")
        invoice_file.write("-------------------------------------------------------------------------------------\n")
        invoice_file.write("Kitta Number: " + land['kitta_number'] + "\n")
        invoice_file.write("City/District: " + land['city_district'] + "\n")
        invoice_file.write("Land Faced: " + land['land_faced'] + "\n")
        invoice_file.write("Date and Time of Return: <datetime>\n")
        invoice_file.write("Duration of Rent: <duration>\n")
        invoice_file.write("Area: " + land['area'] + " anna\n")
    # Confirm successful return invoice generation
    print("Success: Return invoice generated.\n")

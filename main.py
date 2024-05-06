from read import read_file
from operation import rent_land, return_land
def print_banner():
    banner = """
     _                     _   _____            _   _                _____           _                 
    | |                   | | |  __ \          | | (_)              / ____|         | |                
    | |     __ _ _ __   __| | | |__) |___ _ __ | |_ _ _ __   __ _  | (___  _   _ ___| |_ ___ _ __ ___  
    | |    / _` | '_ \ / _` | |  _  // _ \ '_ \| __| | '_ \ / _` |  \___ \| | | / __| __/ _ \ '_ ` _ \ 
    | |___| (_| | | | | (_| | | | \ \  __/ | | | |_| | | | | (_| |  ____) | |_| \__ \ ||  __/ | | | | |
    |______\__,_|_| |_|\__,_| |_|  \_\___|_| |_|\__|_|_| |_|\__, | |_____/ \__, |___/\__\___|_| |_| |_|
                                                            __/ |          __/ |                      
                                                           |___/          |___/              

                                                                            
                                                                            
                                                                by: Manish Karki (N30X)                                                                                                 
    """
    print(banner)

def display_lands(lands):
    # Function to display the availability of lands
    print("--------------------------------Techno Property Nepal---------------------------------")
    print("                               Kamal Pokhari, Kathmandu                               ")
    print("--------------------------------------------------------------------------------------")
    print("Available lands:")
    print("--------------------------------------------------------------------------------------")
    print("Kitta Number | City District | Land Faced | Area | Price")
    print("--------------------------------------------------------------------------------------")
    for land in lands:
        if land["status"] == "Available":
            print(land['kitta_number'] + " | " + land['city_district'] + " | " + land['land_faced'] + " | " + land['area'] + " anna | " + land['price'])
    print("--------------------------------------------------------------------------------------")

    print("\nNot available lands:")
    print("--------------------------------------------------------------------------------------")
    print("Kitta Number | City District | Land Faced | Area | Price")
    print("--------------------------------------------------------------------------------------")
    for land in lands:
        if land["status"] == "Not Available":
            print(land['kitta_number'] + " | " + land['city_district'] + " | " + land['land_faced'] + " | " + land['area'] + " anna | " + land['price'])
    print("--------------------------------------------------------------------------------------")

def main():
    # Print ASCII banner
    print_banner()

    lands = read_file()
    display_lands(lands)

    while True:
        print("\n*************************************************************************************")
        print("\n=====================================================================================")
        print("|                              Transaction menu:                                     |")
        print("======================================================================================")
        print("|                                1. Rent land                                        |")
        print("======================================================================================")
        print("|                                2. Return land                                      |")
        print("======================================================================================")
        print("|                                3. Exit                                             |")
        print("======================================================================================")
        try:
            option = int(input("Choose transaction option (1/2/3): "))
            if option == 1:
                rent_land(lands)
            elif option == 2:
                return_land(lands)
            elif option == 3:
                print("\n----------------------Thank You for Using our system, signing out!!-------------------")
                print("\nExiting program.............")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        except ValueError:
            print("You have provided an Invalid input. Please enter a number (1, 2, or 3).")

    
    '''while True:
        print("\nTransaction menu:")
        print("--------------------------------------------------------------------------------------")
        print("1. Rent land")
        print("2. Return land")
        print("3. Exit")
        option = input("Choose transaction option (1/2/3): ")
        if option == "1":
            rent_land(lands)
        elif option == "2":
            return_land(lands)
        elif option == "3":
            print("\n----------------------Thank You for Using our system, signing out!!-------------------")
            print("\nExiting program.............")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")'''

if __name__ == "__main__":
    main()

from datetime import datetime, timedelta
from read import read_file
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
    """
    print(banner)

def main():
    # Print ASCII banner
    print_banner()
    lands = read_file()
    while True:
        print("\nTransaction menu:")
        print("1. Rent land")
        print("2. Return land")
        print("3. Exit")
        option = input("Choose transaction option (1/2/3): ")
        if option == "1":
            rent_land(lands)
        elif option == "2":
            return_land(lands)
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()


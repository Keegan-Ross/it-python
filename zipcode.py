from banner import banner
banner("ZIP CODE SORTER", "Keegan Ross")

print("Welcome to the Newaygo County zip code sorter")
go_again = True
while go_again == True:
    zip_code = int(input("Please enter a zip code: "))
    if zip_code == 49309:
        print(f"The zip code {zip_code} is for Bitely.")
    elif zip_code == 49312:
        print(f"The zip code {zip_code} is for Brohman.")
    elif zip_code == 49337:
        print(f"The zip code {zip_code} is for Croton & Newaygo.")
    elif zip_code == 49412:
        print(f"The zip code {zip_code} is for Fremont.")
    elif zip_code == 49413:
        print(f"The zip code {zip_code} is for Fremont.")
    elif zip_code == 49327:
        print(f"The zip code {zip_code} is for Grant.")
    elif zip_code == 49349:
        print(f"The zip code {zip_code} is for White Cloud.")
    else:
        print(f"This zip code {zip_code} is not in Newaygo County.")

    if input("Would you like to enter another zip code (Y/N)? ") == "Y":
        continue
    else:
        break
print("Thank you for using Newaygo County Zip Code Sorter. Goodbye!")
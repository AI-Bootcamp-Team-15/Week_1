from ArcheksChef import ArcheksChef
from DonaldChef import DonaldChef
# from ChefGPT-Adwit import ChefGPT-Adwit
from dotenv import load_dotenv

# take environment variables from .env file if exits, otherwise the default ones come from environment variables.  
load_dotenv()  

chefs = [ArcheksChef(), DonaldChef()]

while True:
    print("\n")
    for i in range(len(chefs)):
        print(f"{i} - {chefs[i].name}: {chefs[i].description}")

    print('Type "exit" to terminate script\n')

    chefNumber = input("Select GPT Chef by number: ")
    if  chefNumber.isnumeric() and int(chefNumber) in range(len(chefs)):
        chefs[int(chefNumber)].run()
    else:
        if chefNumber=="exit":
            break;
        print("Wrong number. Can you please try again?\n")

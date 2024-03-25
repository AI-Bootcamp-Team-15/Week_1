from ArcheksChef import ArcheksChef
from ChefGPT-Adwit import ChefGPT-Adwit

chefs = [ArcheksChef(), ChefGPT-Adwit()]


while True:
    print("\n")
    for i in range(len(chefs)):
        print(i, '-', chefs[i].name)

    print('Type "exit" to terminate script\n')

    chefNumber = input("Select GPT Chef by number:\n")
    if  chefNumber.isnumeric() and int(chefNumber) in range(len(chefs)):
        chefs[i].run()
    else:
        if chefNumber=="exit":
            break;
        print("Wrong number\n")

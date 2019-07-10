# DEVELOPING SKILLS #
# THIS GAME IS BASED ON THE BANK SYSTEM OF MALAYSIA (CURRENCY SYSTEM) #
# MIGHT HAVE SOME UNSOLVED ERRORS #
# Hastags are used for readability purpose #
# BY PERI.R #

import random, replit, time, math
from termcolor import cprint
from colorama import *

init()
replit.clear()

# Unrelated
TimeToWork = 0

# levels
money = 10000  # Initialized the cash val
gear_upgrade = 1  # Begins from level 1
security_upgrade = 1  # it will increment based on the options selection
staff_upgrade = 1  # it will increment based on the options selection
customers = 10

################################################################################################################

# Upgrade Prices
gear_upgrade_price = 1000
security_upgrade_price = 500
staff_upgrade_price = 250
advertise_price = 300
paperwork_price = 10

################################################################################################################

# Move location prices
current_location = ""

Penang_price = 500
Johor_price = 700
Pahang_price = 900
Kedah_price = 1100
Perlis_price = 1300
NegeriSembilan_price = 1500
Kelantan_price = 1700

################################################################################################################


# List of locations if they choose above 4
start_locations = ["Selangor", "Perak", "Malacca"]

print(Fore.BLUE + """ 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    ____  ___    _   ____ __   _       ______________  __   __  _______    __
   / __ )/   |  / | / / //_/  | |     / /  _/_  __/ / / /  / / / / ___/   / /
  / __  / /| | /  |/ / ,<     | | /| / // /  / / / /_/ /  / / / /\__ \   / /
 / /_/ / ___ |/ /|  / /| |    | |/ |/ // /  / / / __  /  / /_/ /___/ /  /_/
/_____/_/  |_/_/ |_/_/ |_|    |__/|__/___/ /_/ /_/ /_/   \____//____/  (_)


          A virtual bank that you can manage, own, and destroy.
                         Designed By : PERI.R

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Loading...
""" + Fore.RESET)

time.sleep(3)
print("To start your bank, you persuaded your family and friends to be your customers")
cprint("+10 Customers!", "red")

time.sleep(3)

################################################################################################################

# START LOCATION
print("Now that you got customers ready, you need to find a location for your bank!")
print("1. Selangor")
print("2. Perak")
print("3. Malacca")
choice = input(">> ")

if choice == "1":
    print("You set your location as Selangor")
    current_location = "Selangor"

if choice == "2":
    print("You set your location as Perak")
    current_location = "Perak"

if choice == "3":
    print("You set your location as Malacca")
    current_location = "Malacca"

if choice >= "4":
    random_location = random.choice(start_locations)
    current_location = random_location
    print("You set your location as: " + random_location)

time.sleep(2)

TypesOfPeople = ["a single mom", "a homeless man", "a war veteran", "a small business owner"]
TypesOfAdvertisement = ["a Radio", "a TV Series", "a Movie Series", "a Social Media Site"]


################################################################################################################

# THE ACTUAL PROGRAM WHERE STUFF HAPPENS

def GetToWork():
    replit.clear()
    global money, customers, gear_upgrade, staff_upgrade, security_upgrade, paperwork_price, current_location, gear_upgrade_price, security_upgrade_price, staff_upgrade_price, TimeToWork

    TimeToWork = TimeToWork + 1

    if money <= 0:
        cprint("GAME OVER!", "red", attrs=["bold", "underline"])
        print("""
___________________________________
|#######====================#######|
|#(1)*  BANK NEGARA MALAYSIA  *(1)#|
|#**********           /===\    **#|
|*# {G}               | (") |    #*|
|#*       O N E       | /v\ |    *#|
|#(1)                  \===/   (1)#|
|##=========ONE RINGGIT==========##|
------------------------------------""")
        print("Better luck next time")
        return

    if customers <= 0:
        print(Fore.RED + "GAME OVER!" + Fore.RESET)
        print("Your bank ran out of customers :(")

    if money >= 100000:
        cprint("YOU WON! You got your bank to RM100,000", "green", attrs=["bold"])
        print("But however, there is a recession... so bye")
        time.sleep(3)
        for i in range(1, money):
            time.sleep(0.1)
            money = money - 10000
            print("Your Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
            replit.clear()

            if money <= 0:
                cprint("GAME OVER", "red")
                print(Fore.GREEN + """
___________________________________
|#######====================#######|
|#(1)*  BANK NEGARA MALAYSIA  *(1)#|
|#**********           /===\    **#|
|*# {G}               | (") |    #*|
|#*       O N E       | /v\ |    *#|
|#(1)                  \===/   (1)#|
|##=========ONE RINGGIT==========##|
------------------------------------""" + Fore.RESET)
                print("You won, but also lost")
                return

    ################################################################################################################

    # printing current stats
    print("Current Stats:")
    print("Your Balance: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
    print("Equipment Level: " + str(gear_upgrade))
    print("Security Level: " + str(security_upgrade))
    print("Staff Level: " + str(staff_upgrade))
    print("Customers: " + str(customers))
    print("Current Location: " + current_location)
    print("")
    print("You arrived at work! What do you do?")
    print("1. Give out loans")
    print("2. Accept advertisements")
    print("3. Do paperwork")
    print("4. Invest")
    print("5. Check Donation Bin")
    print("6. Sabotage Competition")
    print("7. Leave work")
    choice = input(">> ")

    ################################################################################################################

    # Give out Loans
    if choice == "1":
        replit.clear()
        wantedLoan = random.randint(100, 1000)

        if money < wantedLoan:
            print("You don't have enough money for this!")
            time.sleep(2)
            GetToWork()

        print(
            "Someone walks in to your bank and asks for a loan of " + Fore.GREEN + "RM" + str(wantedLoan) + Fore.RESET)
        print("Do you accept their offer?")
        yn = input("y/n: ")
        if yn == "y":
            chanceOfReturn = random.randint(1, 2)
            money = money - wantedLoan
            print("You have given the loan of " + Fore.RED + "RM" + str(wantedLoan) + Fore.RESET)
            print("Only time will tell if you get the money back")
            time.sleep(5)

            ################################################################################################################

            # Get your money back (Successful Loan)
            if chanceOfReturn == 1:
                print("You were able to get your money back! And got paid for work!")
                PaidForWork = random.randint(25, 50)
                total = wantedLoan + PaidForWork
                print("You just got a total of: " + Fore.GREEN + "RM" + str(total) + Fore.RESET)
                oney = money + total
                print("Your total balance is: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                time.sleep(4)
                GetToWork()

            ################################################################################################################

            # No money back
            if chanceOfReturn == 2:
                print("You were unable to make any money back.")
                print("You lost: " + Fore.RED + "RM" + str(wantedLoan) + Fore.RESET)
                time.sleep(3)
                GetToWork()

        if yn == "n":
            print("Alright then, no loans at this time!")
            time.sleep(1)
            GetToWork()

    ################################################################################################################

    # Accept Advertisements
    if choice == "2":
        TypesOfAdvertisement_chosen = random.choice(TypesOfAdvertisement)
        Chosen_price = random.randint(50, 100)
        print("A company has decided to use you as an advertiser!")
        print("The company that wants you to advertise is: " + TypesOfAdvertisement_chosen)
        print("They want to pay you: " + Fore.GREEN + "RM" + str(Chosen_price) + Fore.RESET)
        print("Do you accept this offer?")

        yn = input("y/n: ")
        if yn == "y":
            print("You just accepted the offer and got RM" + Fore.GREEN + "RM" + str(Chosen_price) + Fore.RESET)
            money = money + Chosen_price
            print("Your balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
            time.sleep(2)
            replit.clear()
            GetToWork()

        if yn == "n":
            print("You refused the offer, and didn't make any money.")
            time.sleep(2)
            GetToWork()

    ################################################################################################################

    # Do paperwork
    if choice == "3":
        level = gear_upgrade
        print("Doing paperwork...")
        time.sleep(3)
        paperwork_price = paperwork_price * level
        money = money + paperwork_price
        print("You have earned " + Fore.GREEN + "RM" + str(paperwork_price) + Fore.RESET)
        print("Your Balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
        time.sleep(3)
        GetToWork()

    ################################################################################################################

    # invest
    if choice == "4":
        bankInvestment = random.randint(50, 500)
        chanceOfSuccess = random.randint(1, 2)

        # 1 = Successful Investment
        # 2 = Failed Investment

        print("A company has requested that you invest in their company.")
        print("You will give them: " + Fore.GREEN + "RM" + str(bankInvestment) + Fore.RESET)
        print("Do you accept?")
        yn = input("y/n: ")

        if yn == "y":
            replit.clear()
            print("You have given out the loan of " + Fore.GREEN + "RM" + str(
                bankInvestment) + Fore.RESET + " Only time will tell if this was good or not!")
            time.sleep(3)

            ################################################################################################################

            # Successful Investment
            if chanceOfSuccess == 1:
                print("You made a successful investment! And you earned x2 your money!")
                investment = bankInvestment * 2
                money = money + investment
                cprint("You earned: " + Fore.GREEN + "RM" + str(investment) + Fore.RESET)
                print("Your balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                time.sleep(4)
                GetToWork()

            ################################################################################################################

            # Failed Investment
            if chanceOfSuccess == 2:
                money = money - bankInvestment
                print("The business you invested in failed!")
                print("You did not make any money back!")
                print("You wasted: " + Fore.RED + "RM" + str(bankInvestment) + Fore.RESET)
                print("Your balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                time.sleep(4)
                GetToWork()

        if yn == "n":
            replit.clear()
            print("You refused to invest in the business!")
            print("Maybe you would've made more money.")
            time.sleep(3)
            GetToWork()

    ################################################################################################################

    # Check donation bin
    if choice == "5":
        amount = random.randint(10, 15)
        donation = amount * staff_upgrade + TimeToWork
        print("You look into the recycle bin")
        print("There is a total of: " + Fore.GREEN + "RM" + str(donation) + Fore.RESET)
        money = money + donation
        print("Your Balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
        time.sleep(2)
        Menu()

    ################################################################################################################

    # Sabotage Competition
    if choice == "6":
        print("You leave the bank to try and sabotage other bank's advertisements!")
        time.sleep(2)
        print("You were able to take down some of their posters!")
        print("Some customers may not like this though!")
        time.sleep(2)
        customersLost = random.randint(1, 50)
        customersGained = random.randint(1, 50)
        replit.clear()
        print(Fore.RED + "You lost: " + str(customersLost) + " customers" + Fore.RESET)
        print(Fore.GREEN + "But you also gained: " + str(customersGained) + " customers" + Fore.RESET)
        customers = customers - customersLost
        customers = customers + customersGained

        if customersGained > customersLost:
            difference = customersGained - customersLost
            print(Fore.GREEN + "You now have made " + str(difference) + " new customers!")
            time.sleep(2)

        if customersLost > customersGained:
            difference = customersLost - customersGained
            print("You were unable to make any new customers!")
            print(Fore.RED + "You were able to get: " + str(difference) + " customers!" + Fore.RESET)
            time.sleep(2)

        print("Current Customers: " + str(customers))
        time.sleep(5)
        GetToWork()

    ################################################################################################################

    # Leave work
    if choice == "7":
        replit.clear()
        print("Exiting work and going home...")
        time.sleep(3)
        Menu()


################################### MAIN MENU ##################################

def Menu():
    replit.clear()
    global money, customers, gear_upgrade, staff_upgrade, security_upgrade, paperwork_price, current_location, gear_upgrade_price, security_upgrade_price, staff_upgrade_price

    if money <= 0:
        cprint("GAME OVER!", "red", attrs=["bold", "underline"])
        print(Fore.GREEN + """
___________________________________
|#######====================#######|
|#(1)*  BANK NEGARA MALAYSIA  *(1)#|
|#**********           /===\    **#|
|*# {G}               | (") |    #*|
|#*       O N E       | /v\ |    *#|
|#(1)                  \===/   (1)#|
|##=========ONE RINGGIT==========##|
------------------------------------

You won, but also lost. Better luck next time.""" + Fore.RESET)
        return

    if customers <= 0:
        print(Fore.RED + "GAME OVER!" + Fore.RESET)
        print("Your bank ran out of customers :(")

    if money >= 100000:
        cprint("YOU WON! You got your bank to RM100,000", "green", attrs=["bold"])
        print("But however, there is a recession... so bye")
        time.sleep(4)
        for i in range(1, money):
            time.sleep(0.3)
            money = money - 1000
            cprint("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
            replit.clear()

            if money <= 0:
                cprint("GAME OVER", "red")
                print(Fore.GREEN + """
___________________________________
|#######====================#######|
|#(1)*  BANK NEGARA MALAYSIA  *(1)#|
|#**********           /===\    **#|
|*# {G}               | (") |    #*|
|#*       O N E       | /v\ |    *#|
|#(1)                  \===/   (1)#|
|##=========ONE RINGGIT==========##|
------------------------------------""" + Fore.RESET)
                return

    print("Current Balance: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
    print("Current Customers = " + str(customers))
    print("Current Location: " + current_location)
    print("")
    print("Here is the main menu! What do you want to do?")
    print("1. Upgrade Your Equipment (" + Fore.GREEN + "RM" + str(gear_upgrade_price) + Fore.RESET + ") " + str(
        gear_upgrade) + "/5")
    print("2. Upgrade Your Security (" + Fore.GREEN + "RM" + str(security_upgrade_price) + Fore.RESET + ") " + str(
        security_upgrade) + "/5")
    print("3. Upgrade Your Staff (" + Fore.GREEN + "RM" + str(staff_upgrade_price) + Fore.RESET + ") " + str(
        staff_upgrade) + "/5")
    print("4. Advertise (" + Fore.GREEN + "RM" + str(advertise_price) + Fore.RESET + ")")
    print("5. Move location")
    print("6. Go To Work")

    choice = input(">> ")

    ################################################################################################################

    # Equipment Upgrade
    if choice == "1":
        if money < gear_upgrade_price:
            print("You do not have enough for this upgrade!")
            time.sleep(3)
            replit.clear()
            Menu()

        if gear_upgrade == 5:
            print("You can no longer upgrade this!")
            time.sleep(2)
            Menu()

        print("Are you sure you would like to upgrade your Equipment for: " + Fore.GREEN + "RM" + str(
            gear_upgrade_price) + Fore.RESET)

        yn = input("y/n: ")
        if yn == "y":
            money = money - gear_upgrade_price
            gear_upgrade = gear_upgrade + 1
            print("Taken away: " + Fore.RED + "RM" + str(gear_upgrade_price) + Fore.RESET)
            print("Your balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
            print("Your Equipment Level is now: " + str(gear_upgrade))
            gear_upgrade_price = gear_upgrade_price + 500
            time.sleep(3)
            replit.clear()
            Menu()
        if yn == "n":
            replit.clear()
            Menu()

    ################################################################################################################

    # Security Upgrade
    if choice == "2":
        if money < security_upgrade_price:
            print("You do not have enough money for this upgrade!")
            time.sleep(3)
            replit.clear
            Menu()

        if security_upgrade == 5:
            print("You can no longer upgrade this!")
            time.sleep(2)
            Menu()

        print("Are you sure you would like to upgrade your Security for: " + Fore.GREEN + "RM" + str(
            security_upgrade_price) + Fore.RESET)

        yn = input("y/n: ")
        if yn == "y":
            money = money - security_upgrade_price
            security_upgrade = security_upgrade + 1
            print("Taken away: " + Fore.RED + "RM" + str(security_upgrade_price) + Fore.RESET)
            print("Your balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
            print("Your Security Level is now: " + str(security_upgrade))
            security_upgrade_price = security_upgrade_price + 500
            time.sleep(3)
            replit.clear()
            Menu()

        if yn == "n":
            replit.clear()
            Menu()

    ################################################################################################################

    # Staff Upgrade
    if choice == "3":
        if money < staff_upgrade_price:
            print("You do not have enough money for this upgrade!")
            time.sleep(3)
            replit.clear()
            Menu()

        if staff_upgrade == 5:
            print("You can no longer upgrade this!")
            time.sleep(2)
            Menu()

        print("Are you sure you would like to upgrade your Staff for: " + Fore.GREEN + "RM" + str(
            staff_upgrade_price) + Fore.RESET)
        yn = input("y/n: ")

        if yn == "y":
            money = money - staff_upgrade_price
            staff_upgrade = staff_upgrade + 1
            print("Taken away: " + Fore.RED + "RuntimeWarning" + str(staff_upgrade_price) + Fore.RESET)
            print("Your balance is now: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
            print("Your Staff level is now: " + str(staff_upgrade))
            staff_upgrade_price = staff_upgrade_price + 250
            time.sleep(3)
            replit.clear()
            Menu()

        if yn == "n":
            Menu()

    ################################################################################################################

    # Advertise!
    if choice == "4":

        if money < advertise_price:
            print("You do not have enough money for this!")
            time.sleep(2)
            Menu()

        ################################################################################################################

        # Robberies
        chanceOfRobbery = random.randint(1, 100)
        if security_upgrade == 1:
            if chanceOfRobbery < 50:
                replit.clear()
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney = math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "RM" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney
                time.sleep(2)
                Menu()

        if security_upgrade == 2:
            if chanceOfRobbery < 40:
                replit.clear()
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney = math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "RM" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()

        if security_upgrade == 3:
            if chanceOfRobbery < 30:
                replit.clear()
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney = math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "RM" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()

        if security_upgrade == 4:
            if chanceOfRobbery < 20:
                replit.clear()
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney = math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "RM" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()

        if security_upgrade == 5:
            if chanceOfRobbery < 10:
                replit.clear()
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney = math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "RM" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()

        money = money - advertise_price
        replit.clear()
        print("You paid: " + Fore.RED + "RM" + str(advertise_price) + Fore.RESET)
        print("Printing Posters...")
        time.sleep(2)
        print("Uploading Website Adverts...")
        time.sleep(1)
        print("Created Billboard")
        print("")
        new_customers = random.randint(10, 30)
        customers = customers + new_customers

        print("Well done! You have achieved", new_customers, "new customers!")
        NC_Money = new_customers * 5
        money = money + NC_Money
        print("You earned " + Fore.GREEN + "RM" + str(NC_Money) + Fore.RESET + " from new customers signing up!")
        time.sleep(3)
        replit.clear()
        Menu()

    ###################### MOVING BANK LOCATIONS ###################################

    if choice == "5":
        replit.clear()
        print(
            "You have decided to move your bank location to bigger cities for more money! But where do you choose? And what can you afford?")
        print("1. Penang (" + Fore.GREEN + "RM" + str(Penang_price) + Fore.RESET + ")")
        print("2. Johor (" + Fore.GREEN + "RM" + str(Johor_price) + Fore.RESET + ")")
        print("3. Pahang (" + Fore.GREEN + "RM" + str(Pahang_price) + Fore.RESET + ")")
        print("4. Kedah (" + Fore.GREEN + "RM" + str(Kedah_price) + Fore.RESET + ")")
        print("5. Perlis (" + Fore.GREEN + "RM" + str(Perlis_price) + Fore.RESET + ")")
        print("6. Negeri Sembilan(" + Fore.GREEN + "RM" + str(NegeriSembilan_price) + Fore.RESET + ")")
        print("7. Kelantan (" + Fore.GREEN + "RM" + str(Kelantan_price) + Fore.RESET + ")")
        print("8. Go back to the Main Menu")
        new_location = input(">> ")

        ################################################################################################################

        # Penang
        if new_location == "1":
            if money < Penang_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Penang":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")

            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Penang"
                money = money - Penang_price
                print("Taken away: " + Fore.RED + "RM" + str(Penang_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                print("Customers Gained: +100")
                customers = customers + 100
                time.sleep(4)
                Menu()

            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        ################################################################################################################

        # Johor
        if new_location == "2":
            if money < Johor_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Johor":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")

            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Johor"
                money = money - Johor_price
                print("Taken away: " + Fore.RED + "RM" + str(Johor_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                print("Customers Gained: +150")
                customers = customers + 150
                time.sleep(4)
                Menu()

            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        ################################################################################################################

        # Pahang
        if new_location == "3":
            if money < Pahang_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Pahang ":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")

            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Pahang "
                money = money - Pahang_price
                print("Taken away: " + Fore.RED + "RM" + str(Pahang_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                print("Customers Gained: +200")
                customers = customers + 200
                time.sleep(4)
                Menu()

            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        ################################################################################################################

        # Kedah
        if new_location == "4":
            if money < Kedah_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Kedah":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")

            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Kedah"
                money = money - Kedah_price
                print("Taken away: " + Fore.RED + "RM" + str(Kedah_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                print("Customers Gained: +250")
                customers = customers + 250
                time.sleep(4)
                Menu()

            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        ################################################################################################################

        # Perlis
        if new_location == "5":
            if money < Perlis_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Perlis":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")

            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Perlis"
                money = money - Perlis_price
                print("Taken away: " + Fore.RED + "RM" + str(Perlis_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                print("Customers Gained: +300")
                customers = customers + 300
                time.sleep(4)
                Menu()

            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        ################################################################################################################

        # Negeri Sembilan
        if new_location == "6":
            if money < NegeriSembilan_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Negeri Sembilan":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")

            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Negeri Sembilan"
                money = money - NegeriSembilan_price
                print("Taken away: " + Fore.RED + "RM" + str(NegeriSembilan_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                print("Customers Gained: +350")
                customers = customers + 350
                time.sleep(4)
                Menu()

            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        ################################################################################################################

        # Kelantan
        if new_location == "7":
            if money < Kelantan_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Kelantan":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")

            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Kelantan"
                money = money - Kelantan_price
                print("Taken away: " + Fore.RED + "RM" + str(Kelantan_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "RM" + str(money) + Fore.RESET)
                print("Customers Gained: +400")
                customers = customers + 400
                time.sleep(4)
                Menu()

            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        if new_location == "8":
            print("Going back to the main menu")
            time.sleep(2)
            Menu()

    ################################################################################################################

    # Going to work
    if choice == "6":
        print("Driving to work...")
        time.sleep(2)
        GetToWork()


Menu()

################################################################################################################
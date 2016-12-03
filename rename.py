"""This is a strategic game about managing hotels.

The object of the game is to accumulate as much money as possible
in a given number of turns.

"""

from random import randint, choice

from sys import exit

__author__ = "5250994: Arvid Eichner, 5158706: Philipp Gsell"
__copyright__ = "Copyright 2015/2016 – EPR-Goethe-Uni, Arvid Eichner\
Philipp Gsell"
__credits__ = "Hier könnte immer noch Ihre Werbung stehen."
__email__ = "eichner.arvid@gmail.com, philipp.gsell@live.de"

city_names = ["Gießen", "Frankfurt", "Butzbach", "Heidelberg",
              "Ostheim", "Buxtehude", "Mettmann", "Offenbach",
              "Cologne", "Berlin", "Munich", "Unterhachingen",
              "Hagen", "Mückenloch", "Leipzig",
              "Oberhörgern", "Aachen", "Stuttgart", "Hamburg",
              "Darmstadt", ]

list_adjacent = []


def help():
    """ Help Menu

    """
    print("Welcome to the Help-Menu! \n\n\
These are the rules of the game: \n\n\
 You are the owner of a successfull hotel\n\
 and you are now thinking about expanding\n\
 your business. At the start of the game you can choose the following\n\
 values yourself or let them be generated randomly for you:\n\n\
 Number of cities: 5 to 20\n\
 Number of managers in hometown: 5 to 20\n\
 Available rounds: 5 to 40\n\
 Potential profit per city: -20 to 90\n\
 Existing roads between cities\n\n\
 You start the game with no money and should try to accumulate as much\n\
 as possible by the end of the game. The potential profit of a city can \n\
 be earned by building hotels and placing managers in them. \n\
 A hotel without a manager leads to a loss of -20 per round. \n\
 Each day/turn you can choose one of the following four actions by\n\
 entering the following commands: \n\n\
 - Do Nothing: pass \n\
 - Build a hotel: build: city\n\
 - Move number of managers from city1 to city2: move: number, city1, city2\n\
 - Hire a manager: hire: city\n\n\
 Available functions:\n\n\
 - Restart the game: restart\n\
 - Exit the game: exit\n\
 - Help-Menu: help\n\n")


def PrintMatrix():
    """ Create adjacency matrix out of lists

    """
    city_names_abbr = []
    for city in range(len(gListOfInstances)):
        city_names_abbr.append(city_names[city][:2])
    city_names_abbr = " ".join(i for i in city_names_abbr)

    print(" " * 16, city_names_abbr)
    for i in range(len(list_adjacent)):
        print(city_names[i], " " * (15 - len(city_names[i])), list_adjacent[i])


class Cities:
    """ This is the class for city-related values.

    """
    def __init__(self, name, potential_profit, hotel = 0, manager = 0,
                 realised_profit = 0):
        """ This is the constructor for city objects.

        """
        self.name = name
        self.potential_profit = potential_profit
        self.hotel = hotel
        self.manager = manager
        self.realised_profit = realised_profit

    def adjacency_list(self, adjacency):
        """This is the method for saving adjacent cities.

        """
        self.adjacency = adjacency

    def build_hotel(self):
        """This is the method for building hotels.

        """
        self.hotel = 1

    def move_manager(self, managers_moved):
        """This is the method for moving managers.

        """
        self.managers_moved = managers_moved
        self.manager += managers_moved

    def hire_manager(self):
        """This is the method for hiring managers.

        """
        self.manager += 1


def class_assignment(x, number_cities):
    """ Initiate cities as class objects.

    Parameters can be randomly generated or user input,
    depending on user choice. For x: either "potential_profit_random"
    or "player.potential_profit"

    """


    global Gießen, Frankfurt, Butzbach, Heidelberg, Ostheim, Buxtehude, \
        Mettmann, Offenbach, Cologne, Berlin, Munich, Unterhachingen, Hagen, \
        Mückenloch, Leipzig, Oberhörgern, Aachen, Stuttgart, Hamburg, \
        Darmstadt, Trier

    Gießen = Cities("Gießen", potential_profit=x[0])
    Frankfurt = Cities("Frankfurt", potential_profit=x[1])
    Butzbach = Cities("Butzbach", potential_profit=x[2])
    Heidelberg = Cities("Heidelberg", potential_profit=x[3])
    Ostheim = Cities("Ostheim", potential_profit=x[4])

    global gListOfInstances
    gListOfInstances = [Gießen, Frankfurt, Butzbach, Heidelberg, Ostheim]
    # list of all existing instances

    if number_cities >= 6:
        Buxtehude = Cities("Buxtehude", potential_profit=x[5])
        gListOfInstances.append(Buxtehude)
    if number_cities >= 7:
        Mettmann = Cities("Mettmann", potential_profit=x[6])
        gListOfInstances.append(Mettmann)
    if number_cities >= 8:
        Offenbach = Cities("Offenbach", potential_profit=x[7])
        gListOfInstances.append(Offenbach)

    if number_cities >= 9:
        Cologne = Cities("Cologne", potential_profit=x[8])
        gListOfInstances.append(Cologne)

    if number_cities >= 10:
        Berlin = Cities("Berlin", potential_profit=x[9])
        gListOfInstances.append(Berlin)

    if number_cities >= 11:
        Munich = Cities("Munich", potential_profit=x[10])
        gListOfInstances.append(Munich)

    if number_cities >= 12:
        Unterhachingen = Cities("Unterhachingen", potential_profit=x[11])
        gListOfInstances.append(Unterhachingen)

    if number_cities >= 13:
        Hagen = Cities("Hagen", potential_profit=x[12])
        gListOfInstances.append(Hagen)

    if number_cities >= 14:
        Mückenloch = Cities("Mückenloch", potential_profit=x[13])
        gListOfInstances.append(Mückenloch)

    if number_cities >= 15:
        Leipzig = Cities("Leipzig", potential_profit=x[14])
        gListOfInstances.append(Leipzig)

    if number_cities >= 16:
        Oberhörgern = Cities("Oberhörgern", potential_profit=x[15])
        gListOfInstances.append(Oberhörgern)

    if number_cities >= 17:
        Aachen = Cities("Aachen", potential_profit=x[16])
        gListOfInstances.append(Aachen)

    if number_cities >= 18:
        Stuttgart = Cities("Stuttgart", potential_profit=x[17])
        gListOfInstances.append(Stuttgart)

    if number_cities >= 19:
        Hamburg = Cities("Hamburg", potential_profit=x[18])
        gListOfInstances.append(Hamburg)

    if number_cities == 20:
        Darmstadt = Cities("Darmstadt", potential_profit=x[19])
        gListOfInstances.append(Darmstadt)


class Functions:
    """Class for player-specific functions.

    """
    def __init__(self, money = 0, round_profit = 0):
        """This is the constructor for the player object.

        """
        self.money = money
        self.round_profit = round_profit

    def number_of_cities(self):
        """Let player choose number of cities.

        """

        self.input_number_of_cities = input("Please enter the number of \
cities. (5 to 20)")
        if self.input_number_of_cities.isdigit():
            if int(self.input_number_of_cities) in range(5, 21):
                self.input_number_of_cities = int(self.input_number_of_cities)
                print("You chose to play with ", self.input_number_of_cities,
                      " cities.")
                print("Those cities are", city_names[
                                          0:self.input_number_of_cities])
            else:
                print("Unexpected input. Please enter a number between 5 and \
20.")
                self.number_of_cities()

        elif self.input_number_of_cities == "exit":
            print("You have left the game.")
            exit()

        elif self.input_number_of_cities == "restart":
            main()

        elif self.input_number_of_cities == "help":
            help()

        else:
            print("Unexpected input. Please enter a number between 5 and 20.")
            self.number_of_cities()

    def number_of_managers(self):
        """Let player choose number of local managers.

        """
        self.input_number_of_managers = input("Please enter the number of \
managers in your home town. (5 to 20)")
        if self.input_number_of_managers.isdigit():
            if int(self.input_number_of_managers) in range(5, 21):
                print("You chose to play with ", self.input_number_of_managers,
                      " managers.")
                self.input_number_of_managers = \
                    int(self.input_number_of_managers)
            else:
                print("Unexpected input. Please enter a number between \
5 and 20.")
                self.number_of_managers()

        elif self.input_number_of_managers == "exit":
            print("You have left the game.")
            exit()

        elif self.input_number_of_managers == "restart":
            main()

        elif self.input_number_of_managers == "help":
            help()

        else:
            print("Unexpected input. Please enter a number between 5 and 20.")
            self.number_of_managers()

    def available_days(self):
        """Let player choose number of available days.

        """
        self.input_available_days = input("Please enter the number \
of available days/rounds you want to play. (5 to 40)")
        if self.input_available_days.isdigit():
            if int(self.input_available_days) in range(5, 41):
                print("You chose to play with ", self.input_available_days,
                      " days.")
                self.input_available_days = int(self.input_available_days)
            else:
                print("Unexpected input. Please enter a number between \
5 and 40.")
                self.available_days()

        elif self.input_available_days == "exit":
            print("You have left the game.")
            exit()

        elif self.input_available_days == "restart":
            main()

        elif self.input_available_days == "help":
            help()

        else:
            print("Unexpected input. Please enter a number between 5 and 40.")
            self.available_days()

    def input_potential_profit(self):
        """Let player choose potential profit for city i.

        """

        self.potential_profit = []
        for i in range(self.input_number_of_cities):

            checker = True

            while checker:  # exit while loop when input is correct
                            # and proceed to next city

                self.user_input = input("Please enter potential profit \
for %s" % city_names[i])

                if "-" in self.user_input:  # catch neg. numbers because
                                            # they can't be read by "isdigit"
                    self.user_input = self.user_input.lstrip("-")

                    if self.user_input.isdigit():

                        if int(self.user_input) in range(0, 21):
                            self.user_input = int(self.user_input)
                            self.user_input *= -1  # convert to negative
                            # number again
                            self.potential_profit.append(self.user_input)
                            checker = False

                        else:
                            print("Unexpected input. Please enter a number \
between -20 and 90.")
                elif self.user_input.isdigit():  # check for positive numbers

                    if int(self.user_input) in range(0, 91):
                        self.user_input = int(self.user_input)
                        self.potential_profit.append(int(self.user_input))
                        checker = False

                    else:
                        print("Unexpected input. Please enter a number \
between -20 and 90.")
                elif self.user_input == "exit":
                    print("You have left the game.")
                    exit()

                elif self.user_input == "restart":
                    main()

                elif self.user_input == "help":
                    help()

                else:
                    print("Unexpected input. Please enter a number between \
-20 and 90.")


    def matrix(self):
        """This method fills the adjacency matrix with 0.

        """
        for i in range(self.input_number_of_cities):
            list_adjacent.append([0] * (self.input_number_of_cities))

    def hometown(self):
        """This method lets the player choose his hometown.

        """
        chosen_hometown = input("Please enter your desired hometown: ")
        # if valid input for hometown assign attribute else try again
        if chosen_hometown in city_names[0:self.input_number_of_cities]:
            self.chosen_hometown = chosen_hometown
            gListOfInstances[city_names.index(
                chosen_hometown)].build_hotel()   # build hotel in hometown

            for i in range(self.input_number_of_managers):
                gListOfInstances[city_names.index(chosen_hometown)].\
                    hire_manager()  # hire manager in hometown

        elif self.chosen_hometown == "exit":
            print("You have left the game.")
            exit()

        elif self.chosen_hometown == "restart":
            main()

        elif self.chosen_hometown == "help":
            help()

        else:
            print("Invalid hometown. Please try again.")
            self.hometown()

    def increase_money(self, amount):
        """This method increases the players money.

        """
        self.amount = amount
        self.money += amount

    def calculate_round_profit(self):
        """This method calculates the last rounds profit.

        """
        self.round_profit = 0  # set round profit to zero at start of round

        for city in gListOfInstances:

            if city.hotel == 1:

                if city.manager > 0:
                    self.round_profit += city.potential_profit
                    city.realised_profit = city.potential_profit

                else:
                    self.round_profit -= 20
                    city.realised_profit = -20

        self.increase_money(self.round_profit)  # add round profit to total
                                                # money score

player = Functions()

def ConnectedCities():
    """ Let Player choose connected cities for each city

    """
    for i in range(len(gListOfInstances)):
        list_adjacent[i][i] = 1  # Straße zu sich selbst

        a = True  # checker while loop

        while a:

            connected_cities_input = input("Which other cities \
should %s be connected to? When you're done enter next to proceed to the \
next city." % city_names[i])  # instance name gibt namen der stadt zurück

            if connected_cities_input == "next":  # FIX zweite condition frisst er nicht       # enter next to get to next city, oder wenn alle connections gezogen wurden
                print("Connections for", city_names[i], "are complete.")

                gListOfInstances[i].adjacency_list(
                    list_adjacent[i])  # assign binary list of adj. cities of city i to class object adjacency
                a = False

            elif connected_cities_input in city_names:
                if list_adjacent[i][
                    city_names.index(connected_cities_input)] == 1:  # check if cities are already connected
                    print("There is already a connection between", city_names[i], "and", connected_cities_input)

                elif list_adjacent[city_names.index(connected_cities_input)][
                    i] == 1:  # check via symmetry (matrix) if cities are already connected
                    print("There is already a connection between", city_names[i], "and", connected_cities_input)

                else:
                    # for a in range(len(gListOfInstances)):  # scheinbar überflüssiges code stück
                    list_adjacent[i][
                        city_names.index(connected_cities_input)] = 1  # Straße zu der Stadt aus Input Matrix hinzufügen
                    list_adjacent[city_names.index(connected_cities_input)][
                        i] = 1  # Symmetrie Straße von Input zu Stadt

            elif connected_cities_input == "exit":
                print("You have left the game.")
                exit()

            elif connected_cities_input == "restart":
                main()

            elif connected_cities_input == "help":
                help()

            else:  # Fehleingaben, nichts wird als fehleingabe gewertet
                print("Unexpected input. Please enter a city name thats in the list.")

    PrintMatrix()


def random_hometown():
    global random_chosen_hometown
    random_chosen_hometown = choice(gListOfInstances)
    player.chosen_hometown = random_chosen_hometown.name  # assingn random hometown to class object
    random_chosen_hometown.build_hotel()  # build hotel in hometown
    for i in range(number_of_managers_random):
        random_chosen_hometown.hire_manager()


def random_connected_cities():
    for i in range(len(gListOfInstances)):
        for j in range(len(gListOfInstances)):
            if i == j:
                list_adjacent[i][j] = 1  # city is always connected to itself
                list_adjacent[j][i] = 1
            else:
                # for city i randomize connections to all other cities
                list_adjacent[i][j] = randint(0, 1)
                list_adjacent[j][i] = list_adjacent[i][j]

        gListOfInstances[i].adjacency_list(list_adjacent[i])
        # assign binary list of conn. cities of city i to class object adjacency

    print("\nThis is how all cities are connected:\n")
    PrintMatrix()


def matrix_random():
    global list_adjacent
    list_adjacent = []
    # create empty list for Adjacent matrix
    for i in range(number_of_cities_random):
        list_adjacent.append([0] * (number_of_cities_random))


def random_initial_values():
    """Generate random initial game values

    """
    global number_of_cities_random, number_of_managers_random, \
        available_days_random, potential_profit_random

    number_of_cities_random = randint(5, 20)  #### testTTTT mit 5 funktioniert es
    matrix_random()
    number_of_managers_random = randint(5, 20)
    available_days_random = randint(5, 40)
    potential_profit_random = [randint(-20, 90) for i \
                               in range(number_of_cities_random)]
    # create list of random profits for all cities
    class_assignment(potential_profit_random, number_of_cities_random)
    random_hometown()
    random_connected_cities()
    print("\nYou will play with %d cities, %d intial managers and %d available\
 days. \n\nYour hometown is %s." % (number_of_cities_random,
                                    number_of_managers_random, available_days_random,
                                    random_chosen_hometown.name))
    print("\nThose are the potential profits for all cities: \n")
    for i in range(len((potential_profit_random))):
        print(city_names[i], " " * (15 - len(city_names[i])),

              potential_profit_random[i])


def daily_summary():
    print("\nYour hometown is", player.chosen_hometown)
    print("\nCity data overview:")
    print("\nCity (Managers, Hotel, Potential Profit, Realised Profit)\n")

    for i in gListOfInstances:
        print(i.name, " " * (15 - len(i.name)),
              "(%d, %d, %d, %d)" % (i.manager, i.hotel,
                                    i.potential_profit, i.realised_profit))

    print("--------------------------------------------")
    print("- In this round you made a profit of", player.round_profit)
    print("- Your total balance is now:", player.money)
    print("- Total days passed:", days_passed)
    print("-", round_count, "days remaining.")
    print("--------------------------------------------")


def save_score():
    # read part:

    txt_score = open("highscore.txt", "r+")

    a = 0

    for line in txt_score:  # check length of highscore file
        a += 1

    txt_score.seek(0)  # to start at beginning of file
    highscore_list = []
    for entry in txt_score.readlines():
        # read all entries from txt
        highscore_list.append(entry.strip("\n"))

    txt_score.close()

    # write part:

    txt_score = open("highscore.txt", "r+")

    if a == 0:  # if txt empty
        txt_score.write(str(player.money) + "\n")

    else:
        # add currrent score to list, sort and write first 10 elements
        highscore_list.append(str(player.money))

        highscore_list.sort(reverse=True)

        for entry in highscore_list[:10]:
            txt_score.write(entry + "\n")

    txt_score.close()

    # read txt again to print highscore list

    txt_score = open("highscore.txt", "r+")

    for line in txt_score:
        print(line)


def initial_game_values():
    """Set initial game values

    """
    player.number_of_cities()
    player.matrix()
    player.number_of_managers()
    player.available_days()
    player.input_potential_profit()
    class_assignment(player.potential_profit, player.input_number_of_cities)
    player.hometown()
    ConnectedCities()


def main():
    print("\nWelcome to HotelCytoon!\n\n\n\
This game is all about the profit.\n\n\
To learn how to play the game please enter help.\n\n\
You can exit or restart the game at any time by entering exit or restart. \n\n\
Have fun!\n\n")

    a = 0

    global round_count
    round_count = 0

    global days_passed
    days_passed = 0

    checker = 1
    while checker:
        input_method = input("For information about valid inputs please enter \
help.\n\n\
Do you want to choose the initial game values \
yourself? (Yes/No). \nIf not they will be randomly generated for you.\n\n\
")

        if input_method in ["Yes", "YES", "yes", "Y", "y", ]:
            initial_game_values()
            round_count = player.input_available_days
            checker = 0

        elif input_method in ["No", "NO", "no", "N", "n"]:
            random_initial_values()
            round_count = available_days_random
            checker = 0

        elif input_method == "exit":
            print("You have left the game.")
            exit()

        elif input_method == "restart":
            main()

        elif input_method == "help":
            help()



        else:
            print("Unexpected input. Please enter \"Yes\" or \"No\".")

    while round_count > 0:

        if a > 0:  # für 3 züge funktion hire.

            player.calculate_round_profit()
            round_count -= 1
            days_passed += 1
            daily_summary()
            if a == 1:
                gListOfInstances[city_names.index \
                    (action_input_hire)].hire_manager()  # hire manager in city
                print("Your new manager has arrived.")
            else:
                print("\n   Hiring manager...")

            a -= 1
            continue

        action_input = input("\nPlease enter your desired action: ")

        # help
        # rules
        # exit

        if action_input == "pass":
            player.calculate_round_profit()
            round_count -= 1
            days_passed += 1
            daily_summary()

        elif action_input == "exit":
            print("You have left the game.")
            exit()

        elif action_input == "restart":
            main()

        elif action_input == "help":
            help()


        elif "build: " in action_input:
            # filter "build: " to get name of city
            action_input_build = action_input[7:]
            if action_input_build in city_names:  # if valid city name
                if gListOfInstances[city_names.index \
                            (action_input_build)].hotel == 0:  # if no hotel in city
                    player.calculate_round_profit()
                    # calculate profit as soon as valid input but before
                    # making any moves
                    gListOfInstances[city_names.index \
                        (action_input_build)].build_hotel()  # build hotel in city
                    print("You have successfully built a hotel in ",
                          action_input_build)
                    round_count -= 1
                    days_passed += 1
                    daily_summary()
                else:
                    print("There's already a hotel in", action_input_build)
            else:
                print("Invalid city. Please try again.")



        elif "hire: " in action_input:
            # filter "hire: " to get name of city
            action_input_hire = action_input[6:]
            if action_input_hire in city_names:
                if gListOfInstances[city_names.index(action_input_hire)]. \
                        hotel == 1:
                    player.calculate_round_profit()
                    # calculate profit as soon as valid input but before
                    # making any moves

                    print("You will now be hiring a manager for",
                          action_input_hire, "This will take two more days.")
                    a = 3  # kostet 3 Runden / Züge siehe oben
                else:
                    print("You can only hire managers in a city with a hotel.")
                    print("Try building a hotel in", action_input_hire,
                          "first.")
            else:
                print("Invalid city. Please try again.")



        elif "move: " in action_input:
            # filter "move: " to get values for number, city1 and city2
            action_input_move = action_input[6:]
            if action_input_move.count(",") == 2:  # check for input-structure
                # split input into elements
                action_input_values = [i.strip() for i in action_input_move. \
                    split(",")]
                manager_move_number = action_input_values[0]
                city1 = action_input_values[1]
                city2 = action_input_values[2]

                # check for correct and differing city-names
                if city1 and city2 in city_names and city1 != city2:
                    if list_adjacent[city_names.index(city1)] \
                            [city_names.index(city2)] == 1:  # check for connection between cities
                        if manager_move_number.isdigit():
                            manager_move_number = int(action_input_values[0])
                            # check for sufficient amount of managers
                            if manager_move_number <= gListOfInstances[city_names. \
                                    index(city1)].manager:
                                player.calculate_round_profit()
                                # calculate profit as soon as valid input but before
                                # making any moves
                                gListOfInstances[city_names.index(city1)]. \
                                    move_manager(
                                    -1 * manager_move_number)  # lower number of managers of city1 by number of moved managers
                                gListOfInstances[city_names.index(city2)]. \
                                    move_manager(
                                    manager_move_number)  # raise number of managers of city2 by number of moved managers
                                print("You have successfully moved",
                                      manager_move_number, "manager(s) from", city1,
                                      "to", city2)
                                round_count -= 1
                                days_passed += 1
                                daily_summary()
                            else:
                                print("Not enough managers in ", city1, "Please \
choose a lower number.")
                        else:
                            print("Invalid number of managers. Please try again.")
                    else:
                        print("There is no street between", city1, "and", city2)
                else:
                    print("Invalid city. Please try again.")
            else:
                print("Invalid input. Please try again.")

        else:
            print("Invalid input. Please try again.")

    print("No more days left. The game is over.")

    save_score()







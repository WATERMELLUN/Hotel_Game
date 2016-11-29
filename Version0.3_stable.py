## header

from random import randint

city_names = ["Gießen", "Frankfurt", "Butzbach", "Heidelberg",
              "Ostheim", "Buxtehude", "Mettmann", "Offenbach",
              "Cologne", "Berlin", "Munich", "Unterhachingen",
              "Hagen", "Mückenloch", "Leipzig",
              "Oberhörgern", "Aachen", "Stuttgart", "Hamburg",
              "Darmstadt", "Trier"]

list_adjacent = []


def PrintMatrix():
    """ Print matrix

    """
    print(" " * 15, city_names[:len(list_of_instances)])
    for i in range(len(list_adjacent)):
        print(city_names[i],  " " * (15 - len(city_names[i])), list_adjacent[i])

class cities():
    def __init__(self, name, potential_profit, ):  # todo Hier noch weitere Variablen wie Hotel und Manager hinzufügen
        self.name = name
        self.potential_profit = potential_profit

    def roads_to(self, roads_to):  # Method to save cities to which there is a road
        self.roads_to = roads_to

    def adjacency_list(self, adjacency):  # roads_to (binary)
        self.adjacency = adjacency

    def do_nothing(self):
        pass

    def build_hotel(self):
        pass

    def move_manager(self):
        pass

    def hire_manager(self):
        pass


def class_assignment(x):  # parameter x can be randomly generated list or user list, depending on user choice
    # either "potential_profit_random" or "player.potential_profit"

    global Gießen, Frankfurt, Butzbach, Heidelberg, Ostheim, Buxtehude, \
        Mettmann, Offenbach, Cologne, Berlin, Munich, Unterhachingen, Hagen, \
        Mückenloch, Leipzig, Oberhörgern, Aachen, Stuttgart, Hamburg, \
        Darmstadt, Trier

    Gießen = cities("Gießen", potential_profit=x[
        0])  # potential profit eingefügt damit klarer ist worauf sich variable bezieht, kommen noch ein paar dazu
    Frankfurt = cities("Frankfurt", potential_profit=x[1])
    Butzbach = cities("Butzbach", potential_profit=x[2])
    Heidelberg = cities("Heidelberg", potential_profit=x[3])
    Ostheim = cities("Ostheim", potential_profit=x[4])

    try:  # avoid out of range if chosen number of cities < 20
        Buxtehude = cities("Buxtehude", potential_profit=x[5])
        Mettmann = cities("Mettmann", potential_profit=x[6])
        Offenbach = cities("Offenbach", potential_profit=x[7])
        Cologne = cities("Cologne", potential_profit=x[8])
        Berlin = cities("Berlin", potential_profit=x[9])
        Munich = cities("Munich", potential_profit=x[10])
        Unterhachingen = cities("Unterhachingen", potential_profit=x[11])
        Hagen = cities("Hagen", potential_profit=x[12])
        Mückenloch = cities("Mückenloch", potential_profit=x[13])
        Leipzig = cities("Leipzig", potential_profit=x[14])
        Oberhörgern = cities("Oberhörgern", potential_profit=x[15])
        Aachen = cities("Aachen", potential_profit=x[16])
        Stuttgart = cities("Stuttgart", potential_profit=x[17])
        Hamburg = cities("Hamburg", potential_profit=x[18])
        Darmstadt = cities("Darmstadt", potential_profit=x[19])
        Trier = cities("Trier", potential_profit=x[20])

    except IndexError:
        pass  # assign potential profit from list until list ends

    global list_of_instances
    list_of_instances = [Gießen, Frankfurt, Butzbach, Heidelberg, Ostheim]  # list of all existing instances

    try:
        list_of_instances.append(Buxtehude)
        list_of_instances.append(Mettmann)
        list_of_instances.append(Offenbach)
        list_of_instances.append(Cologne)
        list_of_instances.append(Berlin)
        list_of_instances.append(Munich)
        list_of_instances.append(Unterhachingen)
        list_of_instances.append(Hagen)
        list_of_instances.append(Mückenloch)
        list_of_instances.append(Leipzig)
        list_of_instances.append(Oberhörgern)
        list_of_instances.append(Aachen)
        list_of_instances.append(Stuttgart)
        list_of_instances.append(Hamburg)
        list_of_instances.append(Darmstadt)
        list_of_instances.append(Trier)

    except NameError:
        pass  # only append existing instances to list, stop if name-error occurs


class Functions:
    def number_of_cities(self):
        """Let player choose number of cities.

        DIE INSTANZ DER KLASSE IST DER SPIELER SELBST!! ÜBER PLAYER.METHODE KANN DANN VON ÜBERALL AUF DIE FUNKTIONEN
        ZUGEGRIFFEN WERDEN - INSHALLAH

        """

        self.input_number_of_cities = input("Please enter the number of cities. (5 to 20)")
        if self.input_number_of_cities.isdigit():
            if int(self.input_number_of_cities) in range(5, 21):
                self.input_number_of_cities = int(self.input_number_of_cities)
                print("You chose to play with ", self.input_number_of_cities, " cities.")
                print("Those cities are", city_names[
                                          0:self.input_number_of_cities])  # show city names to user WIRD MIT ECKIGEN KLAMMERN AUSGEGEBEN//FIX mit for schleife am besten
            else:
                print("Unexpected input. Please enter a number between 5 and 20.")
                self.number_of_cities()
        else:
            print("Unexpected input. Please enter a number between 5 and 20.")
            self.number_of_cities()

    def number_of_managers(self):
        """Let player choose number of local managers.

        """
        self.input_number_of_managers = input("Please enter the number of managers in your \
home town. (5 to 20)")
        if self.input_number_of_managers.isdigit():
            if int(self.input_number_of_managers) in range(5, 21):
                print("You chose to play with ", self.input_number_of_managers, " managers.")
                self.input_number_of_managers = int(self.input_number_of_managers)
            else:
                print("Unexpected input. Please enter a number between 5 and 20.")
                self.number_of_managers()
        else:
            print("Unexpected input. Please enter a number between 5 and 20.")
            self.number_of_managers()

    def available_days(self):
        """Let player choose number of available days.

        """
        self.input_available_days = input("Please enter the number of available days\
/rounds you want to play. (5 to 40)")
        if self.input_available_days.isdigit():
            if int(self.input_available_days) in range(5, 41):
                print("You chose to play with ", self.input_available_days, " days.")
                self.input_available_days = int(self.input_available_days)
            else:
                print("Unexpected input. Please enter a number between 5 and 40.")
                self.available_days()
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
                            # self.input_potential_profit()

                elif self.user_input.isdigit():  # check for positive numbers
                    if int(self.user_input) in range(0, 91):
                        self.user_input = int(self.user_input)
                        self.potential_profit.append(int(self.user_input))
                        checker = False
                    else:
                        print("Unexpected input. Please enter a number between -20 and\
90.")
                        # self.input_potential_profit()  # todo jeden input neu aufrufen (for loop nicht von vorne beginnnen bei falscher eingabe (schleifen durchlauf wiederholen))
                else:
                    print("Unexpected input. Please enter a number between -20 and\
90.")
                    # self.input_potential_profit()

    def matrix(self):
        # create empty list for AdJAZENTZmadrix

        # fill empty list with 6 sublists of number_of_cities each
        for i in range(self.input_number_of_cities):
            list_adjacent.append([0] * (self.input_number_of_cities))


player = Functions()


def connected_cities():
    """ Let Player choose connected cities for each city

    """
    for i in range(len(list_of_instances)):
        #list_connected_cities = [city_names[i]]
        # fill this list for each city with user input, safe in self.roads_to, reset
        # instance.name since city is always connected to itself
        list_adjacent[i][i] = 1  # Straße zu sich selbst

        a = True  # checker while loop

        while a:

            connected_cities_input = input("Which other cities \
should %s be connected to? When you're done enter next to proceed to the \
next city." % city_names[i])  # instance name gibt namen der stadt zurück

            if connected_cities_input == "next":  # FIX zweite condition frisst er nicht       # enter next to get to next city, oder wenn alle connections gezogen wurden
                print("Connections for", city_names[i], "are complete.")

                list_of_instances[i].roads_to(list_adjacent[i])  # call class function roads_to with list of connected cities as input -> assign each instance its connected cities as list
                a = False

            elif connected_cities_input in city_names:
                if list_adjacent[i][city_names.index(connected_cities_input)] == 1:  # check if cities are already connected
                    print("There is already a connection between", city_names[i], "and", connected_cities_input)

                elif list_adjacent[city_names.index(connected_cities_input)][i] == 1:  # check via symmetry (matrix) if cities are already connected
                    print("There is already a connection between", city_names[i], "and", connected_cities_input)

                else:
                    for a in range(len(list_of_instances)):
                        list_adjacent[i][city_names.index(connected_cities_input)] = 1  # Straße zu der Stadt aus Input Matrix hinzufügen
                        list_adjacent[city_names.index(connected_cities_input)][i] = 1  # Symmetrie Straße von Input zu Stadt

            else:  # Fehleingaben, nichts wird als fehleingabe gewertet
                print("Unexpected input. Please enter a city name thats in the list.")

    PrintMatrix()






def random_initial_values():
    """Generate random initial game values

    """
    global number_of_cities_random, number_of_managers_random, \
        available_days_random, potential_profit_random

    number_of_cities_random = randint(5, 20)
    number_of_managers_random = randint(5, 20)
    available_days_random = randint(5, 40)
    potential_profit_random = [randint(-20, 90) for i in
                               range(number_of_cities_random)]


def daily_summary():
    pass  # todo


def total_profit():
    pass  # todo


def initial_game_values():
    """Set initial game values

    """

    input_method = input("Do you want to choose the initial game values \
yourself? (Yes/No). If not they will be randomly generated.")

    if input_method in ["Yes", "YES", "yes", "Y", "y", ]:
        player.number_of_cities()
        player.matrix()
        player.number_of_managers()
        player.available_days()
        player.input_potential_profit()
        class_assignment(player.potential_profit)
        connected_cities()




    elif input_method in ["No", "NO", "no", "N", "n"]:
        random_initial_values()
        # todo random Straßen zwischen den Städten assignen
        class_assignment(potential_profit_random)  # run class assignment with random values

    else:
        print("Unexpected input. Please enter \"Yes\" or \"No\".")
        initial_game_values()


initial_game_values()





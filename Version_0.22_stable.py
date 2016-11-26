## header

from random import randint

city_names = ["Gießen", "Frankfurt", "Butzbach", "Heidelberg",
              "Ostheim", "Buxtehude", "Mettmann", "Offenbach",
              "Cologne", "Berlin", "Munich", "Unterhachingen",
              "Hagen", "Mückenloch", "Leipzig",
              "Oberhörgern", "Aachen", "Stuttgart", "Hamburg",
              "Darmstadt", "Trier"]

class cities():
    def __init__(self, potential_profit,):  # todo Hier noch weitere Variablen wie Hotel und Manager hinzufügen
        self.potential_profit = potential_profit

    def do_nothing(self):
        pass

    def build_hotel(self):
        pass

    def move_manager(self):
        pass

    def hire_manager(self):
        pass


def number_of_cities():
    """Let player choose number of cities.

    """
    global input_number_of_cities  # global damit später bei def potential profit darauf zugegriffen werden kann.
    input_number_of_cities = input("Please enter the number of cities. (5 to 20)")
    if input_number_of_cities.isdigit():
        if int(input_number_of_cities) in range(5, 21):
            print("You chose to play with ", input_number_of_cities, " cities.")
            input_number_of_cities = int(input_number_of_cities)
        else:
            print("Unexpected input. Please enter a number between 5 and 20.")
            number_of_cities()
    else:
        print("Unexpected input. Please enter a number between 5 and 20.")
        number_of_cities()


def number_of_managers():
    """Let player choose number of local managers.

    """
    input_number_of_managers = input("Please enter the number of managers in your \
home town. (5 to 20)")
    if input_number_of_managers.isdigit():
        if int(input_number_of_managers) in range(5, 21):
            print("You chose to play with ", input_number_of_managers, " managers.")
            input_number_of_managers = int(input_number_of_managers)
        else:
            print("Unexpected input. Please enter a number between 5 and 20.")
            number_of_managers()
    else:
        print("Unexpected input. Please enter a number between 5 and 20.")
        number_of_managers()


def available_days():
    """Let player choose number of available days.

    """
    input_available_days = input("Please enter the number of available days\
/rounds you want to play. (5 to 40)")
    if input_available_days.isdigit():
        if int(input_available_days) in range(5, 41):
            print("You chose to play with ", input_available_days, " days.")
            input_available_days = int(input_available_days)
        else:
            print("Unexpected input. Please enter a number between 5 and 40.")
            available_days()
    else:
        print("Unexpected input. Please enter a number between 5 and 40.")
        available_days()


def input_potential_profit():
    """Let player choose potential profit for city i.

    """
    global potential_profit
    potential_profit = []
    for i in range(input_number_of_cities):
        print("Please enter potential profit for ", city_names[i])
        user_input = input("")

        if "-" in user_input:  # catch neg. numbers because they can't
                                # be read by "isdigit"
            user_input = user_input.lstrip("-")
            if user_input.isdigit():
                if int(user_input) in range(0, 21):
                    user_input = int(user_input)
                    user_input *= -1  # convert to negative number again
                    potential_profit.append(user_input)
                else:
                    print("Unexpected input. Please enter a number between -20 and\
            90.")
                    input_potential_profit()

        elif user_input.isdigit():  # check for positive numbers
            if int(user_input) in range(0, 91):
                user_input = int(user_input)
                potential_profit.append(int(user_input))
            else:
                print("Unexpected input. Please enter a number between -20 and\
90.")
                input_potential_profit()  # todo jeden input neu aufrufen (for loop nicht von vorne beginnnen bei falscher eingabe (schleifen durchlauf wiederholen))
        else:
            print("Unexpected input. Please enter a number between -20 and\
90.")
            input_potential_profit()

def random_initial_values():
    """Generate random initial game values

    """
    global number_of_cities_random, number_of_managers_random, \
        available_days_random, potential_profit_random

    number_of_cities_random = randint(5,20)
    number_of_managers_random = randint(5,20)
    available_days_random = randint(5,40)
    potential_profit_random = [randint(-20,90) for i in
    range(number_of_cities_random)]


def class_assignment(x):

    global Gießen, Frankfurt, Butzbach, Heidelberg, Ostheim, Buxtehude, \
        Mettmann, Offenbach, Cologne, Berlin, Munich, Unterhachingen, Hagen, \
        Mückenloch, Leipzig, Oberhörgern, Aachen, Stuttgart, Hamburg, \
        Darmstadt, Trier

    Gießen = cities(x[0])
    Frankfurt = cities(x[1])
    Butzbach = cities(x[2])
    Heidelberg = cities(x[3])
    Ostheim = cities(x[4])

    try:
        Buxtehude = cities(x[5])
        Mettmann = cities(x[6])
        Offenbach = cities(x[7])
        Cologne = cities(x[8])
        Berlin = cities(x[9])
        Munich = cities(x[10])
        Unterhachingen = cities(x[11])
        Hagen = cities(x[12])
        Mückenloch = cities(x[13])
        Leipzig = cities(x[14])
        Oberhörgern = cities(x[15])
        Aachen = cities(x[16])
        Stuttgart = cities(x[17])
        Hamburg = cities(x[18])
        Darmstadt = cities(x[19])
        Trier = cities(x[20])

    except IndexError:
        pass  # assign potential profit from list until list ends


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
        number_of_cities()
        number_of_managers()
        available_days()
        input_potential_profit()
        # todo den user Straßen zwischen den Städten assignen lassen
        class_assignment(potential_profit)


    elif input_method in ["No", "NO", "no", "N", "n"]:
        random_initial_values()
        # todo random Straßen zwischen den Städten assignen
        class_assignment(potential_profit_random)  # run class assignment with random values

    else:
        print("Unexpected input. Please enter \"Yes\" or \"No\".")
        initial_game_values()

initial_game_values()




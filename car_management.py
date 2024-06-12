class CarManager:
    # stores all car instances created
    all_cars = []
    
    total_cars = 1
    # maybe a nested list. future addition. going to want this to be a instance attribute so it stores services done to specific car rather than all cars. so i'll need to move this
    service_list = {}

    # car_tracker = 0
    # for idx in all_cars:
    #     for key, vals in idx.items():
    #         car_tracker += 1
    
    def __init__ (self, owner, make, model, year, mileage, services=service_list, id=total_cars):
        self.total_cars 
        self._id = CarManager.total_cars
        self._owner = owner
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
    
    def all_cars_list (self):
        new_vehicle = {}
        new_vehicle[f"ID #{self._id}"] = f"{self._year} {self._make} {self._model}"
        CarManager.total_cars += 1
        return CarManager.all_cars.append(new_vehicle)

    def __str__ (self):
        return f"{self._owner}'s {self._make} {self._model}"


    
def car_application():

    def exit_message():
        return print("\nThank you for using Garrett's Car Manager! Have a nice day")
    
    def add_a_car():
        car_owner = input("Owner's Name: ")
        car_make = input("Car Make: ")
        car_model = input("Model: ")
        car_year = input("Year: ")

        # if car year is not a number, or not 4 digits, or less than 0
        if car_year.isnumeric() is False or (len(str(car_year)) == 4) is False or (int(car_year) >  0) == False:
            while car_year.isnumeric() is False or (len(str(car_year)) == 4) is False or (int(car_year) > 0) == False:
                print("Car year must be a numeric value in YYYY format!")
                car_year = input("Year: ")

        car_mileage = input("Current Mileage: ")
        # if you car milesage isnt a number or less than 0
        if car_mileage.isnumeric() is False or (int(car_mileage) > 0) == False:
            while car_mileage.isnumeric() is False or (int(car_mileage) > 0) == False:
                print("Car mileage must be a numeriic value greater than 0!")
                car_mileage = input("Current Mileage: ")
        
        # takes the car_owner input from above and uses that owners name to save the CarManager instance inside of
        car_owner = CarManager(car_owner, car_make, car_model, car_year, car_mileage)
        # this adds the new car to the all cars dict
        car_owner.all_cars_list()
        print("Car added to Car Manager. Returning to main menu...")
        menu_selection()

    def view_all_cars():
        print("\n---- LIST OF CARS ----")
        print(CarManager.all_cars)
        print("\n1. Main Menu 2. Quit")
        exit_screen = input("Make your selection: ")
        if int(exit_screen) != 1 or int(exit_screen) != 2:
            while (int(exit_screen) == 1) is False and (int(exit_screen) == 2) is False:
                print("Enter 1 or 2!")
                exit_screen = input("Make your selection: ")
        if exit_screen == "1":
            menu_selection()
        else:
            exit_message()

    def view_total_cars():
        print(f"\nTotal number of cars: {CarManager.total_cars - 1}")
        menu_selection()

    def see_cars_details():
        for idx in CarManager.all_cars:
            for key, vals in idx.items():
                print(f"{key} : {vals}")
        car_selection = input("\nWhich ID would you like to see the details of?: ")
        print(CarManager.all_cars[int(car_selection)])


    def service_a_car():
        pass

    def update_mileage():
        pass

    def menu_selection():
        menu_select = (input("""
            ---- WELCOME! ----
            1. Add a car
            2. View all cars
            3. View total number of cars
            4. See a car's details
            5. Service a car
            6. Update mileage
            7. Quit
            Make your selection: """))
        
        if menu_select.isnumeric() is False or int(menu_select) < 1 or int(menu_select) > 7:
                print("Invalid Option. Must input a number between 1 and 7")
                menu_selection()
        

        if menu_select == "1":
            add_a_car()
        elif menu_select == "2":
            view_all_cars()
        elif menu_select == "3":
            view_total_cars()
        elif menu_select == "4":
            see_cars_details()
        elif menu_select == "5":
            service_a_car()
        elif menu_select == "6":
            update_mileage()
        elif menu_select == "7":
            exit_message()
    
    menu_selection()



print(car_application())
print(CarManager.all_cars)
print(CarManager.total_cars)
print(CarManager.car_tracker)
print(CarManager.total_cars)
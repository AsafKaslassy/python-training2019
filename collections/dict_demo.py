"""
You should complete the following code in order to create a dict object that holds key value pairs describing the following cars.
The key should be the car id number. The value should be a tuple that describes the car.
5324334, mazda 6, 2014, 2000
2434343, mazda 3, 2013, 1600
5234343, ford kuga, 2014, 1500
Once you complete the code, you should execute it and debug it in order to see the content of cars as one of the watches the debugger allows us to set.
cars = {
5324334: (______, 2014, 2000),
          _______: ('mazda 3', 2013, 1600),
5234343: ('ford kuga', ____, 1500)
}
print(cars)
"""


class Cars:
    def add_car_parameters(self, id_number, model, year, engine):
        self.id_number = id_number
        self.model = model
        self.year = year
        self.engine = engine

        #  = {self.id : (self.year, self.model, self.engine), self.year : '', }
        car_details = {self.id_number: (self.year,
                                        self.model,
                                        self.engine)}
        print("Inside dictionary: ")
        print(car_details.items())

        return car_details.items()


car1 = Cars()

cars = car1.add_car_parameters(5324334, "mazda 3", 2014, 2000), \
       car1.add_car_parameters(2434343, "mazda 6", 2013, 1600), \
       car1.add_car_parameters(5234343, "ford kuga", 2014, 1500)

print("\nOutside dictionary: ")
for x in cars:
    print(f"Print cars: {cars}".split('dict_items'))
    print(f"Print x: {x}")

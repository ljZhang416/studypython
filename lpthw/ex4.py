#cars 100
cars = 100
#space_in_a_car 4.0
space_in_a_car = 4.0
#drivers 30
drivers = 30
#passengers 90
passengers = 90
#cars_not_driven与cars - drivers相等
cars_not_driven = cars - drivers
#cars_drivers与drivers相等
cars_driven = drivers
#carpool_capacity与cars_driven*space_in_a_car相等
carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car与passengers/cars_driven相等
average_passengers_per_car = passengers / cars_driven


#打印“cars可用的有多少”
print("These are", cars ,"cars available.")
#打印“drivers可用的有多少”
print("Thers are", drivers, "drivers available.")
#打印“cars_not_driven有多少”
print("There are", cars_not_driven, "empty cars today.")
#打印“carpool_capacity有多少”
print("We can transport", carpool_capacity, "people today.")
#打印“passeng可用的有多少”
print("We have", passengers, "to carpool today.")
#打印“average_passengers_per_car可用的有多少”
print("We need to put about", average_passengers_per_car, "in each car.")



cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("USING THE NORMAL METHOD OF (CONCATENATE) STRINGS")
# Blank line
print()
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each cars.")
print()

print(">" * 50)
print(">" * 50)
print()
# This code is simillar to the code above but the format is different.
# USING THE (str) METHOD THE SAME CODE CAN BE WRITTEN IN THIS FORMAT.
print("USING THE (str) method:")
# Blank line
print()
print("There are " + str(cars) + " cars available.")
print("There are only " + str(drivers) + " drivers available.")
print("There will be " + str(cars_not_driven) + " empty cars today.")
print("We can transport " + str(carpool_capacity) + " people today.")
print("We have " + str(passengers) + " to carpool today.")
print('We need to put about ' + str(average_passengers_per_car) + ' in each cars.')
print()

print(">" * 50)
print(">" * 50)
print()
# This code is simillar to the code above but the format is different.
# USING THE (.format) METHOD THE SAME CODE CAN ALSO BE WRITTEN IN THIS FORMAT.
print("USING THE (.format) method:")
# Blank line
print()
print("There are {} cars available.".format(cars))
print("There are only {} drivers available.".format(drivers))
print("There will be {} empty cars today.".format(cars_not_driven))
print("We can transport {} people today.".format(carpool_capacity))
print("We have {} to carpool today.".format(passengers))
print("We need to put about {} in each cars.".format(average_passengers_per_car))



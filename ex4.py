#Existing Car numbers have
cars = 100
#How many passenagers could be fit each car.
space_in_a_car = 4.0
#Existing driver numbers have
drivers = 30
#Existing passenagers need to be transported
passenagers = 90
#Cars number which will not be driven as no more drivers
cars_not_driven = cars - drivers
#Cars number that will be driven to transport passenagers
cars_driven = drivers
#Total capacity for existing driven cars to transport passenagers
carpool_capacity = cars_driven * space_in_a_car
#average passenagers nunber for one car
average_passenagers_per_car = passenagers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars not.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passenagers, "to carpool today.")
print("we need to put about", average_passenagers_per_car, "in each car.")
# number of cars
cars = 100
# the space available inside a car
space_in_a_car = 4
# number of drivers online
drivers = 30
# number on passengers online
passengers = 90
# the number of cars that are stationary
cars_not_driven = cars - drivers
# nubmer of cars on the road
cars_driven = drivers
# the amount of passengers that we can carry
carpool_capacity = cars_driven * space_in_a_car
# average number of people in cars
average_passenger_per_car = passengers / cars_driven

#how many cars on the road right now
print("There are", cars, "cars available.")
#how many drivers on the road right now
print("There are only", drivers, "drivers available.")
# how many cars not working
print("There will be", cars_not_driven, "empty cars today.")
# how much capacity out there in cars
print("We can transport", carpool_capacity, "people today.")
# how many people we have to transport today
print("We have", passengers, "to carpool today.")
# the average number of people out there per car
print("We need to put out", average_passenger_per_car, "in each car.")

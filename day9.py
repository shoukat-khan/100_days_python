# #dictionaries \

# # dictionary is a collection of key value pairs
# dictionary = { "key1": "value1", "key2": "value2", "key3": "value3" }
# print(dictionary)

# #using loop

# for key in dictionary:
#     print(key, dictionary[key])

# #dictionary in a list    

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", ]}
#     ,
#     {
#         "country": "Germany",
#         "visits": 5}]
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 
# def add_new_country(country,visits,list_of_cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = visits
#     new_country["cities"] = list_of_cities
#     travel_log.append(new_country)
#     return travel_log


# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")


#bidding game 
import os
from os import system
def cls():
    os.system('cls' if os.name=='nt' else 'clear')




bidding ={}

def add_bid(name ,bid ):
    bidding[name]= bid 


def find_winner(bidding):
    highest_bid = 0
    winner = ""
    for key in bidding:
        if bidding[key] > highest_bid:
            highest_bid = bidding[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")
#main program

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    add_bid(name,bid)
    more_bids = input("Do you want to add more bids? (yes/no): ")
    if more_bids == "no":
        find_winner(bidding)
        break
    cls()
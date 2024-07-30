#HIGH_LOW_GAME



import random


#list of dictionary having name insta follower and the country of the celebrity

celebrity = [
    {"name": "Selena Gomez", "follower": 167, "country": "USA"},
    {"name": "Cristiano Ronaldo", "follower": 250, "country": "Portugal"},
    {"name": "Dwayne Johnson", "follower": 220, "country": "USA"},
    {"name": "Kylie Jenner", "follower": 200, "country": "USA"},
    {"name": "Kim Kardashian", "follower": 210, "country": "USA"},
    {"name": "Lionel Messi", "follower": 220, "country": "Argentina"},
    {"name": "Beyonce", "follower": 200, "country": "USA"},
    {"name": "Neymar", "follower": 150, "country": "Brazil"},
    {"name": "Taylor Swift", "follower": 200, "country": "USA"},
    {"name": "Justin Bieber", "follower": 200, "country": "Canada"}
]

#how to check the data type of the follower key in the dictionary

print (type(celebrity[0]["follower"]))



#function to select a random celebrity from the list

def select_celebrity():
    return random.choice(celebrity)

#function to compare the follower of the celebrity

def compare_follower(celebrity1, celebrity2):
    if celebrity1["follower"] > celebrity2["follower"]:
        return "a"
    else:
        return "b"
    

def game():
    print("Welcome to the Higher Lower Game")
    score = 0
    game_over = False
    celebrity1 = select_celebrity()
    #check if the celebrity1 and celebrity2 are same
    celebrity2 = select_celebrity()
    while celebrity1 == celebrity2:
        celebrity2 = select_celebrity()
    while not game_over:
        print(f"Compare A: {celebrity1['name']}, a {celebrity1['country']}, {celebrity1['follower']} followers.")
        print("vs")
        print(f"Against B: {celebrity2['name']}, a {celebrity2['country']}, {celebrity2['follower']} followers.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if guess == compare_follower(celebrity1, celebrity2):
            score += 1
            print(f"Correct! Current score: {score}")
            celebrity1 = celebrity2
            while celebrity1 == celebrity2:
              celebrity2 = select_celebrity()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

game()


    
    

    


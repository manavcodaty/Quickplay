import random

players_names = []
players = {}




chance_dict={1:"Advance to the nearest utility. If unowned, you may buy it from the bank. If owned, you may buy it from the bank. If owned, throw dice and pay owner ten times the amount thrown",
             2:"Advance to the nearest railroad. If unowned you may buy it from the bank. If owned, pay owner twice the rent to which they are otherwise entitled.",
             3:"Take a trip to Reading Railroad. If you pass go, collect $200.",
             4:"GO TO JAIL. GO DIRECTLY TO JAIL DO NOT PASS GO DO NOT COLLECT $200",
             5:"Go back 3 spaces.",
             6:"Advance to Illinois Avenue. If you pass go, collect $200.",
             7:"Speeding Fine $15",
             8:"Advance to St. Charles Place. If you pass go, collecct $200",
             9:"Your building loan matures, collect $150",
             10:"You have been elected chairman of the board. Pay each player $50",
             11:"Advance to the nearest railroad. If unowned you may buy it from the bank. If owned, pay owner twice the rent to which they are otherwise entitled.",
             12:"Bank pays you dividend of $50",
             13:"Advance to go, collect $200",
             14:"Advance to Boardwalk",
             15:"Get out of jail free. This card may be kept until needed or sold.",
             16:"Make general repairs on all your property. For each house, pay $25, for each hotel, pay $100"}
chest_dict={1:"Get out of jail free. This card may be kept until needed or sold.",
            2:"Income tax refund, collect $20",
            3:"Advance to go. Collect $200",
            4:"School fees. Pay $50",
            5:"Holiday fund matures collect $100",
            6:"Life insurance matures. collect $100",
            7:"You inherit $100",
            8:"Receive $25 consultancy fee",
            9:"You are assessed for street repairs. pay $40 per house and $115 per hotel you own.",
            10:"GO TO JAIL GO DIRECTLY TO JAIL DO NOT PASS GO DO NOT COLLECT $200",
            11:"From sale of stock, you get $50.",
            12:"You have won second prize in a beauty contest. Collect $10",
            13:"Bank error in your favor. collect $200.",
            14:"Doctor's fees. Pay $50",
            15:"It's your birthday! Collect $10 from every player.",
            16:"Hospital fees. Pay $100"}
properties = [{
    "name": "Meditaranian Avenue",
    "price": 60,
    "rent": 2,
    "house_cost": 50,
    "hotel_cost": 50,
    "mortgage": 30,
    "color": "brown",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Community Chest",
    "On community chest": True
},
{
    "name": "Baltic Avenue",
    "price": 60,
    "rent": 4,
    "house_cost": 50,
    "hotel_cost": 50,
    "mortgage": 30,
    "color": "brown",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Income Tax",
    "price": 200
},
{
    "name": "Reading Railroad",
    "price": 200,
    "rent": 25,
    "mortgage": 100,
    "owner": None
},
{
    "name": "Oriental Avenue",
    "price": 100,
    "rent": 6,
    "house_cost": 50,
    "hotel_cost": 50,
    "mortgage": 50,
    "color": "light blue",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Chance",
    "On chance": True
},
{
    "name": "Vermont Avenue",
    "price": 100,
    "rent": 6,
    "house_cost": 50,
    "hotel_cost": 50,
    "mortgage": 50,
    "color": "light blue",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Connecticut Avenue",
    "price": 120,
    "rent": 8,
    "house_cost": 50,
    "hotel_cost": 50,
    "mortgage": 60,
    "color": "light blue",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Jail",
    "In jail": True
},
{
    "name": "St Charles Place",
    "price": 140,
    "rent": 10,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 70,
    "color": "pink",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Electric Company",
    "price": 150,
    "owner": None
},
{
    "name": "States Avenue",
    "price": 140,
    "rent": 10,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 70,
    "color": "pink",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Virginia Avenue",
    "price": 160,
    "rent": 12,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 80,
    "color": "pink",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Pennsylvania Railroad",
    "price": 200,
    "rent": 25,
    "mortgage": 100,
    "owner": None
},
{
    "name": "St James Place",
    "price": 180,
    "rent": 14,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 90,
    "color": "orange",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Community Chest",
    "On community chest": True
},
{
    "name": "Tennessee Avenue",
    "price": 180,
    "rent": 14,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 90,
    "color": "orange",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "New York Avenue",
    "price": 200,
    "rent": 16,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 100,
    "color": "orange",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Free Parking",
    "Free parking": True
},
{
    "name": "Kentucky Avenue",
    "price": 220,
    "rent": 18,
    "house_cost": 150,
    "hotel_cost": 150,
    "mortgage": 110,
    "color": "red",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "St. James Place",
    "price": 180,
    "rent": 14,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 90,
    "color": "orange",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Tennessee Avenue",
    "price": 180,
    "rent": 14,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 90,
    "color": "orange",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "New York Avenue",
    "price": 200,
    "rent": 16,
    "house_cost": 100,
    "hotel_cost": 100,
    "mortgage": 100,
    "color": "orange",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Pacific Avenue",
    "price": 300,
    "rent": 26,
    "house_cost": 200,
    "hotel_cost": 200,
    "mortgage": 150,
    "color": "green",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "North Carolina Avenue",
    "price": 300,
    "rent": 26,
    "house_cost": 200,
    "hotel_cost": 200,
    "mortgage": 150,
    "color": "green",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Pennsylvania Avenue",
    "price": 320,
    "rent": 28,
    "house_cost": 200,
    "hotel_cost": 200,
    "mortgage": 160,
    "color": "green",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Park Place",
    "price": 350,
    "rent": 35,
    "house_cost": 200,
    "hotel_cost": 200,
    "mortgage": 175,
    "color": "dark blue",
    "owner": None,
    "houses": 0,
    "hotel": False
},
{
    "name": "Boardwalk",
    "price": 400,
    "rent": 50,
    "house_cost": 200,
    "hotel_cost": 200,
    "mortgage": 200,
    "color": "dark blue",
    "owner": None,
    "houses": 0,
    "hotel": False
}
]

class Player():
    def __init__(self, name, money=1500, position=1, properties=0, in_jail=False, turns_in_jail=0, jail_card=0):
        self.name = name
        self.money = money
        self.position = position
        self.properties = properties
        self.in_jail = in_jail
        self.turns_in_jail = turns_in_jail
        self.jail_card = jail_card
    def dice_roll(self):
        return random.randint(1, 6)
        
        
def start():
    count = 1
    num_players = int(input("How many players are there? "))
    for i in range(num_players):
        name = input("What is player {}'s name? ".format(i+1))
        players_names.append(Player(name))
        players["player" + str(count)] = Player(name)
        
    print("The game has started!")
        
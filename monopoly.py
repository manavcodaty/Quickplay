
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
    def __init__(self, name, money, position, properties, in_jail, turns_in_jail, get_out_of_jail_card, on_go):
        self.name = name
        self.money = money
        self.position = position
        self.properties = properties
        self.in_jail = in_jail
        self.turns_in_jail = turns_in_jail
        self.get_out_of_jail_card = get_out_of_jail_card
        self.on_go = on_go
    
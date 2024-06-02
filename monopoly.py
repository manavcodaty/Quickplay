import random






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
'''
Properties:
List of dictionaries where every index is a dictionary representing a property on the board.
The index is equal to the players position on the board
'''
properties =[
    {
    "name": "Mediterranean Avenue",
    "price": 60,
    "rent": 2,
    "house_cost": 50,
    "hotel_cost": 50,
    "mortgage": 30,
    "color": "brown",
    "owner": None,
    "houses": 0,
    "hotel": False,
    "position": 1
    },
    {
        "name": "Community Chest",
        "On community chest": True,
        "position": 2,
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
        "hotel": False,
        "position": 3,
    },
    {
        "name": "Income Tax",
        "price": 200,
        "position": 4,
    },
    {
        "name": "Reading Railroad",
        "price": 200,
        "rent": 25,
        "mortgage": 100,
        "owner": None,
        "position": 5,
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
        "hotel": False,
        "position": 6,
        
    },
    {
        "name": "Chance",
        "On chance": True,
        "position": 7,
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
        "hotel": False,
        "position": 8,
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
        "hotel": False,
        "position": 9,
    },
    {
        "name": "Jail",
        "In jail": True,
        "Just visiting": True,
        "position": 10,
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
        "hotel": False,
        "position": 11,
    },
    {
        "name": "Electric Company",
        "price": 150,
        "owner": None,
        "position": 12,
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
        "hotel": False,
        "position": 13,
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
        "hotel": False,
        "position": 14,
    },
    {
        "name": "Pennsylvania Railroad",
        "price": 200,
        "rent": 25,
        "mortgage": 100,
        "owner": None,
        "position": 15,
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
        "hotel": False,
        "position": 16,
    },
    {
        "name": "Community Chest",
        "On community chest": True,
        "position": 17,
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
        "hotel": False,
        "position": 18,
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
        "hotel": False,
        "position": 19,
    },
    {
        "name": "Free Parking",
        "Free parking": True,
        "position": 20,
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
        "hotel": False,
        "position": 21,
    },
    {
        "name": "Chance",
        "On chance": True,
        "position": 22,

    },
    {
        "name": "Indiana Avenue",
        "price": 220,
        "rent": 18,
        "house_cost": 150,
        "hotel_cost": 150,
        "mortgage": 110,
        "color": "red",
        "owner": None,
        "houses": 0,
        "hotel": False,
        "position": 23,
        
    },
    {
        "name": "Illinois Avenue",
        "price": 240,
        "rent": 20,
        "house_cost": 150,
        "hotel_cost": 150,
        "mortgage": 120,
        "color": "red",
        "owner": None,
        "houses": 0,
        "hotel": False,
        "position": 24,
        
    },
    {
        "name": "B&O Railroad",
        "price": 200,
        "rent": 25,
        "mortgage": 100,
        "owner": None,
        "position": 25,
        
    },
    {
        "name": "Atlantic Avenue",
        "price": 260,
        "rent": 22,
        "house_cost": 150,
        "hotel_cost": 150,
        "mortgage": 130,
        "color": "yellow",
        "owner": None,
        "houses": 0,
        "hotel": False,
        "position": 26,
    },
    {
        "name": "Ventnor Avenue",
        "price": 260,
        "rent": 22,
        "house_cost": 150,
        "hotel_cost": 150,
        "mortgage": 130,
        "color": "yellow",
        "owner": None,
        "houses": 0,
        "hotel": False,
        "position": 27,
        
    },
    {
        "name": "Water Works",
        "price": 150,
        "owner": None,
        "position": 28,
        
    },
    {
        "name": "Marvin Gardens",
        "price": 280,
        "rent": 24,
        "house_cost": 150,
        "hotel_cost": 150,
        "mortgage": 140,
        "color": "yellow",
        "owner": None,
        "houses": 0,
        "hotel": False,
        "position": 29,
        
    },
    {
        "name": "Go To Jail",
        "Go to jail": True,
        "position": 30,
        
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
        "hotel": False,
        "position": 31,

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
        "hotel": False,
        'position': 32,
    },
    {
        "name": "Community Chest",
        "On community chest": True,
        "position": 33,
        
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
        "hotel": False,
        "position": 34,
    },
    {
        "name": "Short Line Railroad",
        "price": 200,
        "rent": 25,
        "mortgage": 100,
        "owner": None,
        "position": 35,
    },
    {
        "name": "Chance",
        "On chance": True,
        "position": 36,
        
    },
    {
        "name": "Luxury Tax",
        "price": 75,
        "position": 37,
        
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
        "hotel": False,
        "position": 38,
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
        "hotel": False,
        "position": 39,
        
    },
    {
        "name": "Go",
        "Go": True,
        "position": 40,
    
    }
    
]
    

class Player():
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 1
        self.properties = []
        self.in_jail = False    
        self.turns_in_jail = 0
        self.have_jail_card = False
    def dice_roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        self.position += total
        return total, self.position
    def calc_current_position(self):
        for item in properties:
            if item['position'] == self.position:
               current_position = item['name']
               return current_position
    def display_player_box(self, current_position):
        print("-----------------------------------------------------------------------")
        print(f"Player: {self.name}")
        print(f"Money: ${self.money}")
        print(f"Position: {current_position}")
        print(f"Properties: {self.properties}")
        # Add more player info here 
        print("-----------------------------------------------------------------------")
        

        
        
        
class Game():
    def __init__(self):
        self.players = []
        self.turn = 0
        self.chance_cards = list(chance_dict.keys())
        self.chest_cards = list(chest_dict.keys())
    def go_logic(self):
        player = self.players[self.turn]
        if player.position > 40:
            player.position -= 40
            player.money += 200
    def initialize_game(self):
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            name = input("Enter player name: ")
            new_player = Player(name)
            self.players.append(new_player)
            
    
        
    def draw_board(self):
        board = ["   21   22   23   24   25   26   27   28   29   30  31\n"
                "  +------------------------------------------------------+\n"
                "  |FREE|KENT|CHNC|INDI|ILLI|B&O |ATLN|VENT|WATR|MRVN|GOTO|\n"
                "  |PARK|AVE |????|AVE |AVE |RAIL|AVE |AVE |WRKS|GARD|JAIL|\n"
                "  +------------------------------------------------------+\n"
                "  |NEWY|                                            |PACI|\n"
                "20|AVE |                                            |AVE |32\n"
                "  +----+                                            +---+-\n"
                "  |TENN|                                            |NCAR|\n"
                "19|AVE |                                            |AVE |33\n"
                "  +----+                                            +----+\n"
                "  |COMM|                                            |COMM|\n"
                "18|CHST|                                            |CHST|34\n"
                "  +----+                                            +----+\n"
                "  |STJA|                                            |PENN|\n"
                "17|PLCE|                                            |AVE |35\n"
                "  +----+                                            +----+\n"
                "  |PENN|                                            |SHRT|\n"
                "16|RAIL|                                            |LINE|36\n"
                "  +----+                                            +----+\n"
                "  |VIRG|                                            |CHNC|\n"
                "15|AVE |                                            |????|37\n"
                "  +----+                                            +----+\n"
                "  |STAT|                                            |PARK|\n"
                "14|AVE |                                            |PLCE|38\n"
                "  +----+                                            +----+\n"
                "  |ELEC|                                            |LUXR|\n"
                "13|COMP|                                            |TAX |39\n"
                "  +----+                                            +----+\n"
                "  |STCH|                                            |BRD |\n"
                "12|PLCE|                                            |WALK|40\n"
                "  +------------------------------------------------------+\n"
                "  | IN |CONN|VERM|CHNC|ORNT|READ|INCM|BLTC|COMM|MDTN|PASS|\n"
                "  |JAIL|AVE |AVE |????|AVE |RAIL|TAX |AVE |CHST|AVE | GO |\n"
                "  +-------------------------------------------------+----+\n"
                "    11   10   9    8    7    6    5    4    3    2    1  \n"]
        for line in board[0].split('\n'):
            print(line)
            
 
            

    def play(self):
        '''
        Game loop that cycles between players and their turns
        '''
        for player in self.players:
            #code for player turn
            print("xxxxxxxx")

# Create a new game instance
game = Game()
game.initialize_game()  # Initialize the game
game.play()  # Start the game


    
        
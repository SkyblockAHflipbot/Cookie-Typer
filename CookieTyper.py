import pygame
#making pygame work
import random
#making random work
import pickle
#making pickle work 

pygame.init()
#pygame initation
pygame.display.set_caption("Cookie Typer")
#pygame display name on bar windws tag thing 

#Beginning class player 
class Player:
    #fiunction for player class
    def __init__(self) -> None:
        #base balance 
        self.balance = 0
        #base achievments
        self.achievements = []

#Beggining class keyboard
class KeyBoard:
    #Function for keyboard class
    def __init__(self) -> None:
        #base price
        self.price = 10
        #base amount
        self.amount = 0
        #base upgrades for that building 
        self.upgrades = 0
        #base upgrade price 
        self.upgrade_price = 100
    #Function for the output per building
    def bps(self):
        #multipling output with upgrades display
        return 1 * self.amount * 2 ** self.upgrades

#function for laptop class
class Laptop:
    #base price
    def __init__(self) -> None:
        #base amount
        self.price = 100
        #base price
        self.amount = 0
        #base upgrades
        self.upgrades = 0
        #base upgrade price
        self.upgrade_price = 1000
#funtion for output
    def bps(self):
        #mult output with upgrades display
        return 12.5 * self.amount * 2 ** self.upgrades

#class for gamingpc
class GamingPC:
    #function for values
    def __init__(self) -> None:
        #base price
        self.price = 1000
        #base amount
        self.amount = 0
        #base upgrades
        self.upgrades = 0
        #baase upgrade price
        self.upgrade_price = 10000
#function for bps
    def bps(self):
        #upgrades x bps 
        return 125 * self.amount * 2 ** self.upgrades

#class for server
class Server:
    #function for sevr values
    def __init__(self) -> None:
        #price base
        self.price = 10000
        #base amount
        self.amount = 0
        #base upgrades
        self.upgrades = 0
        #base upgrades price
        self.upgrade_price = 100000
#bos function
    def bps(self):
        #investments x bps
        return 1500 * self.amount * 2 ** self.upgrades

#class for supercomputer
class SuperComputer:
    #function for supercomputer
    def __init__(self) -> None:
        #base price
        self.price = 100000
        #base amount
        self.amount = 0
        #base upgrades
        self.upgrades = 0
        #base upgrade price
        self.upgrade_price = 1000000
#base bps function
    def bps(self):
        #upgrades x amount
        return 25000 * self.amount * 2 ** self.upgrades

#class quantumcomputer
class QuantumComputer:
    #funtion quantumcomputer
    def __init__(self) -> None:
        #base price
        self.price = 1000000
        #base amount
        self.amount = 0
        #base upgrades
        self.upgrades = 0
        #base upgrade price 
        self.upgrade_price = 10000000

    def bps(self):
        return 500000 * self.amount * 2 ** self.upgrades

class AI:
    def __init__(self) -> None:
        self.price = 10000000
        self.amount = 0
        self.upgrades = 0
        self.upgrade_price = 100000000

    def bps(self):
        return 10000000 * self.amount * 2 ** self.upgrades

class QuantumAI:
    def __init__(self) -> None:
        self.price = 100000000
        self.amount = 0
        self.upgrades = 0
        self.upgrade_price = 1000000000

    def bps(self):
        return 1000000000 * self.amount * 2 ** self.upgrades

class DysonSphere:
    def __init__(self) -> None:
        self.price = 1000000000
        self.amount = 0
        self.upgrades = 0
        self.upgrade_price = 10000000000

    def bps(self):
        return 10000000000 * self.amount * 2 ** self.upgrades

class BitCoinMiner:
    def __init__(self) -> None:
        self.player = Player()
        self.total_earned = 0
        self.screen = pygame.display.set_mode((1200, 900))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.BuildingTypes = [KeyBoard(), Laptop(), GamingPC(), Server(), SuperComputer(), QuantumComputer(), AI(), QuantumAI(), DysonSphere()]

    def BuyBuilding(self, building):
        if self.player.balance >= building.price:
            self.player.balance -= building.price
            building.price *= 1.15
            building.amount += 1
        if building.__class__ not in self.player.achievements:
            self.player.achievements.append(building.__class__)

    def SellBuilding(self, building):
        if building.amount > 0:
            building.price /= 1.15
            self.player.balance += building.price / 2
            building.amount -= 1
            if building.__class__ in self.player.achievements:
                self.player.achievements.append(building.__class__)

    def BuyUpgrade(self, building):
        if self.player.balance >= building.upgrade_price:
            self.player.balance -= building.upgrade_price
            building.upgrade_price *= 10
            building.upgrades += 1

    def click(self):
        self.player.balance += 1

    def CalcBPF(self):
        BPF = (sum([building.bps() for building in self.BuildingTypes]
                   ) / 60) * 1.01 * len(self.player.achievements)
        return BPF

    def draw(self):
        self.screen.fill((110, 64, 21))
        self.screen.blit(self.font.render(
            f"Balance: {round(self.player.balance, 2)}", True, (0, 0, 0)), (10, 10))
        self.screen.blit(self.font.render(
            f"BPS: {round(self.CalcBPF() * 60, 2)}", True, (0, 0, 0)), (10, 40))
        self.screen.blit(self.font.render(
            f"Achievements: {len(self.player.achievements)}", True, (0, 0, 0)), (10, 850))

        y_pos = 70
        for building in self.BuildingTypes:
            self.screen.blit(self.font.render(
                f"{building.__class__.__name__}: {building.amount}", True, (0, 0, 0)), (10, y_pos))
            self.screen.blit(self.font.render(
                f"Price: {round(building.price, 2)}", True, (0, 0, 0)), (10, y_pos + 30))
            self.screen.blit(self.font.render(
                f"{building.__class__.__name__} upgrades: {building.upgrades}", True, (0, 0, 0)), (400, y_pos))
            self.screen.blit(self.font.render(
                f"Price: {round(building.upgrade_price, 2)}", True, (0, 0, 0)), (400, y_pos + 30))
            y_pos += 60

        pygame.display.update()

    def save(self):
        with open("save.pickle", "wb") as f:
            pickle.dump([self.player, self.BuildingTypes], f)
    
    def load(self):
        try:
            with open("save.pickle", "rb") as f:
                self.player, self.BuildingTypes = pickle.load(f)
        except:
            pass


    def run(self):
        self.load()
        while True:
            self.clock.tick(60)
            self.player.balance += self.CalcBPF()
            self.total_earned += self.CalcBPF()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save()
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    self.click()
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[0])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[0])
                    else:
                        self.BuyBuilding(self.BuildingTypes[0])
                if event.type == pygame.KEYUP and event.key == pygame.K_2:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[1])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[1])
                    else:
                        self.BuyBuilding(self.BuildingTypes[1])
                if event.type == pygame.KEYUP and event.key == pygame.K_3:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[2])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[2])
                    else:
                        self.BuyBuilding(self.BuildingTypes[2])
                if event.type == pygame.KEYUP and event.key == pygame.K_4:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[3])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[3])
                    else:
                        self.BuyBuilding(self.BuildingTypes[3])
                if event.type == pygame.KEYUP and event.key == pygame.K_5:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[4])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[4])
                    else:
                        self.BuyBuilding(self.BuildingTypes[4])
                if event.type == pygame.KEYUP and event.key == pygame.K_6:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[5])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[5])
                    else:
                        self.BuyBuilding(self.BuildingTypes[5])
                if event.type == pygame.KEYUP and event.key == pygame.K_7:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[6])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[6])
                    else:
                        self.BuyBuilding(self.BuildingTypes[6])
                if event.type == pygame.KEYUP and event.key == pygame.K_8:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[7])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[7])
                    else:
                        self.BuyBuilding(self.BuildingTypes[7])
                if event.type == pygame.KEYUP and event.key == pygame.K_9:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[8])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[8])
                    else:
                        self.BuyBuilding(self.BuildingTypes[8])


Game = BitCoinMiner()
Game.run()

import math

class Zombie:
    '''
    Simple Zombie class to track a zombie's state and support methods:
    move, take_arrows, and calculate number of rounds a zombie has been active. (Generating new zombies at random distances is hanled outside this module.)
    '''
    def __init__(self, name, distance, speed, health, round_created=None, round_killed=None, alive=True):
        self.name = name
        self.distance = distance
        self.speed = speed
        self.health = health
        self.round_created = round_created
        self.round_killed = round_killed
        self.alive = alive
        self.ETA = math.ceil(distance/speed)

    def __repr__(self) -> str:
        # return self.__class__.__name__ + str(self.__dict__) ... use to see all attributes
        print_keys = ('name', 'alive', 'distance', 'speed', 'ETA', 'health')
        result = self.__class__.__name__ + '{' 
        result += ', '.join(f'{k}: {self.__dict__[k]}' for k in print_keys)
        result += '}'
        return result
        
    def move(self) -> int:
        '''Move Zombie's position to max(0, self.distance - self.speed), returning Zombie's new distance to player.
        '''
        if not(self.alive):
            raise RuntimeError(f'Tried to move a dead Zombie {self.name}') 
        self.distance = max(0, self.distance - self.speed)
        self.ETA = math.ceil(self.distance/self.speed)
        return self.distance

    def suffer_arrows(self, arrows: int) -> int:
        '''Update Zombie's health after taking arrow hits, returnig Zombie's remaining health. Raise errors if number of arrows exceeds Zombie's health.
        '''
        if not(self.alive):
            raise RuntimeError(f'Shooting {arrows} arrows at an already dead Zombie {self.name}')
        
        self.health = max(0, self.health - arrows)
        if self.health == 0:
            self.alive = False
        return self.health

    def active_rounds(self, final_game_round: int) -> int:
        '''Zombie's active rounds including the round they entered and exited.
        '''
        if self.alive:
            return final_game_round - self.round_created + 1
        else:
            return self.round_killed - self.round_created + 1

    def priority(self):
        '''Used by Player to measure the urgency of shooting arrows at a zombie. Low means urgent. Measured as ETA (number of rounds until zombie reaches player), then health (kill weak zombies first), then zombie name (lowest lexagraphical name in ASCI). In python, a pair of tuples (a0, a1, a2) and (b0, b1, b2) are ordered by comparing a0 to b0, then a1 to b1, then a2 to b2, etc.
        '''
        if not(self.alive):
            raise ValueError(f'Calling priority on a dead zombie {self.name}.')

        return (self.ETA, self.health, [ord(c) for c in self.name])
    
    @classmethod
    def TESTME(cls, arrows_per_zombie = 0, MAX_ROUNDS = 10):
        '''Create some Zombies. Move them. Shoot at them. Normally, zombies will be orchestrated by a Game. But this runs a simple, stand-alone version of that.
        
        We expect Chuck to win the race given his initial distance (20) and speed (8).
        '''
        zombie_attributes = [
            {'name': 'Abe', 'distance': 10, 'speed': 1, 'health': 5},
            {'name': 'Bill', 'distance': 200, 'speed': 40, 'health': 20},
            {'name': 'Chuck', 'distance': 20, 'speed': 8, 'health': 10}
        ]       

        zombies = [Zombie(**z) for z in zombie_attributes]

        print(f'\nAt each round, shoot {arrows_per_zombie} arrows at each living zombie.\n')
        
        print(f'{"="*40}\nInitial Zombies\n{"="*40}')
        for z in zombies:
            print(z)
            if z.alive:
                print(f'Priority (ETA, health, ascii_name:  {z.priority()}\n')
            else:
                print('This zombie is dead\n.')

        for round in range(1, 5):
            print(f'{"="*40}\nEnd of Round {round}\n{"="*40}')
            # advance Zombies
            for z in zombies:
                if z.alive:
                    z.move()
            for z in zombies:
                if z.alive:
                    z.suffer_arrows(arrows_per_zombie)
            for z in zombies:
                print(z)
            priorities = [(z.priority(), z.name) for z in zombies if z.alive]
            priorities.sort()
            print(f'Priorities: {priorities}\n')

                
def main():
    print("\nRun a test game with no arrows ... expect to die.\n")
    Zombie.TESTME(arrows_per_zombie=0)

    print("\n\nRun a test game with 5 arrows at each zombie per round ... expect to live.\n")
    Zombie.TESTME(arrows_per_zombie=5)


if __name__ == "__main__":
    main()
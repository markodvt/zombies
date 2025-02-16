import random
import math

'''Defines a class Zombie that does the following:
- tracks zombie's state (name, distance, speed, health, rounds until killed, alive=T or F)
- moves a zombie (returning it's remaining distance after the move)
- hits a zombie with arrows (returning it's remaining health)
-- TESTME (a Zombie class method) runs a couple games ... one with no arrows, one with arrows

This version lacks any class or encapsulation of the actual Game.

This version doesn't make use of the return values of move or hit_arrows. It just updates zombie state for every zombie, and then updates the global game variables after each round.

This version doesn't allocate arrows to the most urgent zombie targets. It just shoots x arrows at every zombie.

** Added a MAX_ROUNDS = 50 setting to prevent an infinite game. In prior version, the no arrows game terminates (player eaten) but the other game never ends ... new live zombies appear in every round, alongside other live zombies.
'''

class Zombie:

    zack_count = 0

    def __init__(self, name, distance, speed, health, round_created=None, round_killed=None, alive=True):
        self.name = name
        self.init_distance = distance
        self.distance = distance
        self.init_health = health
        self.health = health
        self.speed = speed
        self.round_created = round_created
        self.round_killed = round_killed
        self.alive = alive
        self.time_to_player = math.ceil(distance/speed)

    def __repr__(self):
        print_keys = ('name', 'alive', 'distance', 'health')
        result = self.__class__.__name__ + '{' 
        result += ', '.join(f'{k}: {self.__dict__[k]}' for k in print_keys)
        result += '}'
        return result
        
    def move(self):
        '''Move Zombie's position to max(0, self.distance - self.speed), returning Zombie's new distance to player.
        '''
        if not(self.alive):
            raise RuntimeError(f'Tried to move a dead Zombie {self.name}') 
        self.distance = max(0, self.distance - self.speed)
        return self.distance

    def hit_arrows(self, arrows):
        '''Update Zombie's health after taking arrow hits, returnig Zombie's remaining health. Raise errors if number of arrows exceeds Zombie's health.
        '''
        if not(self.alive):
            raise RuntimeError(f'Shooting {arrows} arrows at an already dead Zombie {self.name}')
        
        self.health = max(0, self.health - arrows)
        if self.health == 0:
            self.alive = False
        return self.health

    @classmethod
    def generate_random(cls):
        '''TODO - make this random. Starting with simple, static constructor.
        '''
        cls.zack_count = cls.zack_count + 1
        inputs = ('Zack ' + str(cls.zack_count), 100, 10, 50)
        new_zombie = Zombie(*inputs)
        return new_zombie

    @classmethod
    def TESTME(cls, arrows_per_zombie = 0, MAX_ROUNDS = 10):
        '''Creates some Zombies. At each round, the zombies move. Ends when a zombie's distance reaches 0.
        No arrows yet, so zombies just keep advancing!! We expect Chuck to win the race given his initial distance (20) and speed (8).
        Round 1: Chuck starts d=20, ends d=12; Round 2: Chuck d=12 drops to d=4; Round 3: Chuck reaches d=0; Game stops.
        
        Adding poor version of random zombies ... presently they're all the same, named "Zack".
                
        '''

        # Initialize Game by creating zombies, setting round = 1, setting MAX_ROUNDS 
        game_round = 1
        zombies = [Zombie("Abe", 10, 1, 5), Zombie("Bill", 200, 40, 20), Zombie("Chuck", 20, 8, 10)]
        for zombie in zombies:
            print(f'Zombie created: {zombie}')

        print(f'\nAt each round, shoot {arrows_per_zombie} arrows at each living zombie.\n')
        
        # TODO - improve performance later freezing dead zombies; for now, just keep updating them all but track if any are alive
        numb_live_zombies = sum(z.alive for z in zombies) 
        min_distance = min(z.distance for z in zombies)

        while (min_distance > 0) and (numb_live_zombies > 0) and (game_round <= MAX_ROUNDS):
            print(f'Round: {game_round} ==========================================')

            # Generate more zombies ...
            print(f'Generating two new zombies ... should be random, but starting with static.')
            for i in range(2):
                zombies.append(Zombie.generate_random())
            
            # Print initial state of zombies:
            print(f'State at start ............')
            for z in zombies:
                print(z) 

            # Move each non-dead zombie:
            for z in zombies:
                if z.alive:
                    z.move()
            
            # Shoot a fixed number of arrows at each non-dead zombie:
            for z in zombies:
                if z.alive:
                    z.hit_arrows(arrows_per_zombie)

            # Display each zombie after moves and arrows    
            print(f'State at end ..........')   
            for z in zombies:
                print(z) 

            # Advance the round number and update the min distance and number of live zombies   
            game_round += 1
            min_distance = min(z.distance for z in zombies)
            numb_live_zombies = sum(z.alive for z in zombies) 
 
            # If all zombies are dead, player survived; otherwise rounds halted when a zombie's distance closed to zero.
        if game_round >= MAX_ROUNDS:
            print(f'\nYou survived {MAX_ROUNDS} rounds, time is up.\n')
        elif numb_live_zombies > 0:
            print(f'\nYou are dead, eaten by {[z.name for z in zombies if (z.alive and not(z.distance))]}!\n')
        else:
            print("\nYou survived, all zombies are terminated!\n")


# Start by tracking game as global variables. Later probably a good idea to create a Game class

def main():
    print("Run a test game with no arrows ... expect to die.\n\n")
    Zombie.TESTME(arrows_per_zombie=0)

    print("\n\nRun a test game with 10 arrows at each zombie per round ... expect to live.\n\n")
    Zombie.TESTME(arrows_per_zombie=10)

if __name__ == "__main__":
    main()
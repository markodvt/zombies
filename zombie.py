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
        return self.distance

    def hit_arrows(self, arrows: int) -> int:
        '''Update Zombie's health after taking arrow hits, returnig Zombie's remaining health. Raise errors if number of arrows exceeds Zombie's health.
        '''
        if not(self.alive):
            raise RuntimeError(f'Shooting {arrows} arrows at an already dead Zombie {self.name}')
        
        self.health = max(0, self.health - arrows)
        if self.health == 0:
            self.alive = False
        return self.health

    def active_rounds(self, final_game_round: int) -> int:
        '''Calculate number of game rounds the zombie has been active, including the round it was created, to and including the round it was shot or the game ended.
        e.g. if created in round 2 and game ended in round 5, then return 4 = (5-2) + 1 for rounds 2, 3, 4, 5
        '''
        if self.alive:
            return final_game_round - self.round_created + 1
        else:
            return self.round_killed - self.round_created + 1
    
    @classmethod
    def TESTME(cls, arrows_per_zombie = 0, MAX_ROUNDS = 10):
        '''Creates some Zombies. At each round, the zombies move. Ends when a zombie's distance reaches 0.
        No arrows yet, so zombies just keep advancing!! We expect Chuck to win the race given his initial distance (20) and speed (8).
        Round 1: Chuck starts d=20, ends d=12; Round 2: Chuck d=12 drops to d=4; Round 3: Chuck reaches d=0; Game stops.                
        '''
        zombie_attributes = [
            {'name': 'Abe', 'distance': 10, 'speed': 1, 'health': 5},
            {'name': 'Bill', 'distance': 200, 'speed': 40, 'health': 20},
            {'name': 'Chuck', 'distance': 20, 'speed': 8, 'health': 10}
        ]       

        zombies = [Zombie(**z) for z in zombie_attributes]

        game_round = 1

        for zombie in zombies:
            print(f'Zombie created: {zombie}')

        print(f'\nAt each round, shoot {arrows_per_zombie} arrows at each living zombie.\n')
        
        numb_live_zombies = sum(z.alive for z in zombies) 
        min_distance = min(z.distance for z in zombies)

        while (min_distance > 0) and (numb_live_zombies > 0) and (game_round <= MAX_ROUNDS):
            print(f'Round: {game_round} ==========================================')
           
            # Print initial state of zombies:
            print(f'State at start ............')
            for z in zombies:
                print(z) 

            # Move each non-dead zombie:
            for z in zombies:
                if z.alive:
                    z.move()
            
            # Check if player was killed
            killers = [z for z in zombies if (z.distance == 0 and z.health > 0)]

            # Shoot a fixed number of arrows at each non-dead zombie:
            if not(killers):
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
            print(f'\nYou are dead, eaten by {killers}!\n')
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
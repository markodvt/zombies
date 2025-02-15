class Zombie:
    def __init__(self, name, distance, speed, health, rounds=0):
        self.name = name
        self.distance = distance
        self.speed = speed
        self.health = health
        self.rounds = 1
        self.alive = True

    def __repr__(self):
        return f'Zombie: name: {self.name}, distance: {self.distance}, speed: {self.speed}, health: {self.health}, rounds: {self.rounds}, alive: {self.alive}'
    
    def move(self):
        '''Move Zombie's position to max(0, self.distance - self.speed), returning Zombie's new distance to player.
        '''
        if not(self.alive):
            raise RuntimeError(f'Tried to move a dead Zombie {self.name}') 
        self.distance = max(0, self.distance - self.speed)
        self.rounds = self.rounds + 1
        return self.distance

    def hit_arrows(self, arrows):
        '''Update Zombie's health after taking arrow hits, returnig Zombie's remaining health. Raise errors if number of arrows exceeds Zombie's health.
        '''
        if not(self.alive):
            raise RuntimeError(f'Shooting {arrows} arrows at an already dead Zombie {self.name}')
        if arrows > self.health:
            raise RuntimeError(f'Shooting {arrows} arrows at a Zombie {self.name} with health only {self.health}')
        arrows_used = min(self.health, arrows)
        self.health = self.health - arrows_used
        if self.health == 0:
            self.alive = False
        return self.health

    @classmethod
    def TESTME(self):
        '''Creates some Zombies. At each round, the zombies move. Ends when a zombie's distance reaches 0.
        No arrows yet, so zombies just keep advancing!! We expect Chuck to win the race given his initial distance (20) and speed (8).
        Round 1: Chuck starts d=20, ends d=12; Round 2: Chuck d=12 drops to d=4; Round 3: Chuck reaches d=0; Game stops.
        '''
        game_round = 1
        zombies = [Zombie("Abe", 10, 1, 5), Zombie("Bill", 200, 40, 20), Zombie("Chuck", 20, 8, 10)]
        for zombie in zombies:
            print(f'Zombie created: {zombie}')
        min_distance = min(z.distance for z in zombies)
        while min_distance > 0:
            print(f'Round: {game_round} ........................................')
            print(f'State at start ............')
            for z in zombies:
                print(z) 
            for z in zombies:
                z.move()
            print(f'State at end ..........')   
            for z in zombies:
                print(z) 
            game_round += 1
            min_distance = min(z.distance for z in zombies)
 
# Start by tracking game as global variables. Later probably a good idea to create a Game class

def main():
    Zombie.TESTME()

if __name__ == "__main__":
    main()
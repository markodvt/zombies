from zombie import Zombie
from zombie_generator import Zombie_generator
from player import Player
from priority_queue import Priority_queue

'''A Game represewnts the state of a roster of Zombies and the state of the Player over a sequence of rounds.
'''

class Game:
    '''Game state includes a player (just one for now), a list of named_zombies, a current round (default to 1), and max_rounds (to prevent infinite games).

    Each round of the game:
    - advance the current_round by one
    - player refills their quiver to quiver_capacity
    - all existing (live) zombies advance, in order they entered the game; first one to reach player kills the player
    - new zombies appear at random (non-zero) distances
    - player shoots all arrows, prioritizing zombies closest to player; "closest" is measured as distance/speed (which zombies will reach player soonest) 

    At each round, move all zombies (even if player had been killed), as verbose mode prints the final positions at end of round, not at death of player.

    Track zombies using two data structures: 
    - zombie array (attached to Game) tracks zombies in the order they were created, which also is the order they move.
    - priority queue (attached to Player) that references the zombies in the order they should be shot with arrows.

    Player uses a priority_queue (updated at each round) to prioritize shooting arrows at zombies with lowest ETA.

    In the event of ties in ETA, you should shoot the zombie with the lower health.
    If zombies are also tied in health, you should shoot the zombie with the lexicographically smaller name (in ASCI).
    '''
    
    def __init__(self, player, named_zombies, zombie_generator, priority_queue=None, max_rounds=1000, current_round=1, status='Not started'):
        # TODO - add game settings to control 
        self.player = player
        self.zombies = named_zombies
        self.zombie_generator = zombie_generator
        self.max_rounds = max_rounds
        self.current_round = current_round
        self.status = status
        

    def __repr__(self):
        '''Display current state of the Game
        '''
        return self.__class__.__name__ + str(self.__dict__)

    def generate_random_zombie(self):
        return self.zombie_generator()
    
    def play_round(self):
        '''Implement this to orchestrate the actions in the round, then advance current_round by 1.
        Returns True if player survives round, False if player is dead (game ends).
        '''
        if not(self.player.alive):
            raise RuntimeError("Player is dead. Tried to start round " + self.current_round + " but game should already have ended when player was killed in round " + self.player.round_killed)

        # Update round status
        if self.status != 'Not started':
            raise RuntimeError(f'Attempted to start a new round, in a round aleady started; round: {self.current_round}')

        self.status = 'Round in progress'
        
        # Refill player's arrows
        self.player.remaining_arrows = self.player.quiver_capacity
        player_lives = self.player.alive
        print("Starting Round with these initial zombie positions ... ")
        print(self.summary())

        # Advance all live zombies
        for z in self.zombies:
            if z.alive:
                new_dist = z.move()
                if player_lives & (new_dist == 0):
                    player_lives = False
                    self.player.killed(z, self.current_round)

        if player_lives:
            # Generate new zombies
            print(f'Generating two new zombies ....')
            for i in range(2):
                z = self.generate_random_zombie()
                self.zombies.append(z)

            # Recalculate player's zombie_queue based on new zombie positions
            # copy of live zombies
            pq = Priority_queue()
            for z in self.zombies:
                if z.alive:
                    pq.push(z, z.priority())
            
            self.priority_queue = pq
        
            print("Zombies advanced, new were generated, ... ")
            print(self.summary())

            # TODO - move this logic into a player method !!!
            while (self.player.remaining_arrows > 0 and not(pq.empty())):
                z = pq.pop()
                arrows_to_shoot = min(z.health, self.player.remaining_arrows)
                print(f'Shooting {arrows_to_shoot} arrows at zombie {z}')
                z.suffer_arrows(arrows_to_shoot)
                self.player.remaining_arrows -= arrows_to_shoot
            self.status = 'Round completed'
            return True
        else:
            self.status = 'Round completed'
            return False

    def prep_next_round(self):
        '''Returns True if game is over.
        '''
        if self.status != 'Round completed':
            raise RuntimeError("Can't prep for next round unless current round is marked completed.")
        
        if not(self.player.alive):
            return True

        if self.current_round == self.max_rounds:
            self.status = "Survived Max Rounds!!"
            return True

        self.current_round += 1
        self.status = 'Not started'
        return False

    def play_game(self):
        player_alive = self.player.alive
        if not(player_alive):
            raise ValueError("Can't start a game if player is already dead.")
        game_over = False
        while (player_alive and not(game_over)):
            # print(self.summary())
            player_alive = self.play_round()
            game_over = self.prep_next_round()
        print(self.summary())
        if game_over:
            print(f'\n{self.status}\n')


    def summary(self):
        result = ('=' * 40)
        result += '\nGAME SUMMARY\n'
        result += '=' * 40
        result += '\nPlayer ' + self.player.name + ' is: ' + ('ALIVE' if self.player.alive else 'DEAD')
        result += '\nCurrent Round: ' + str(self.current_round) + ' ... Status: ' + self.status      
        result += '\nPlayer: ' + str(self.player)
        result += '\nZombies:\n'
        for z in self.zombies:
            result += '    ' + str(z) + '\n'
        return result

    @classmethod
    def TestMe(cls):

        zombie_inputs = [
            ("Abe", 10, 1, 5), 
            ("Bill", 200, 40, 20),
            ("Chuck", 20, 8, 10)
        ]

        random_zombie_config = {
            'random_seed': 42,
            'max_rand_distance': 100,
            'max_rand_speed': 40,
            'max_rand_health': 25
        }

        zombie_generator = Zombie_generator(**random_zombie_config)
        priority_queue = Priority_queue()

        player1 = Player('Steve', quiver_capacity = 10)
        player2 = Player('Jimmy', quiver_capacity = 50)
        
        game1 = Game(player = player1, named_zombies = [Zombie(*z) for z in zombie_inputs], zombie_generator = zombie_generator, priority_queue = priority_queue, max_rounds = 10)
        game2 = Game(player = player2, named_zombies = [Zombie(*z) for z in zombie_inputs], zombie_generator = zombie_generator, max_rounds = 10)
        
        print('PLAY GAME ONE ... Player = Steve, can shoot only 10 arrows per round ...\n\n')
        game1.play_game()

        print('\nPLAY GAME TWO ... Player = Jimmy, can shoot only 50 arrows per round ...\n\n')
        game2.play_game()

def main():
    Game.TestMe()

if __name__ == '__main__':
    main()


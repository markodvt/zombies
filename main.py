from zombie import Zombie

'''A Game represewnts the state of a roster of Zombies and the state of the Player over a sequence of rounds.
'''

class Player:
    '''Player has a name and arrow_capacity. 
    TODO - implement strategy later so player can prioritize their arrows.
    TODO - may want to remove 'survived_rounds' later, unless multiple players.
    '''
    def __init__(self, name, quiver_capacity, alive=True, entered_in_round = 1, killed_in_round = None, killed_by = None):
        self.name = name
        self.quiver_capacity = quiver_capacity
        self.alive = True
        self.entered_in_round = entered_in_round
        self.killed_in_round = killed_in_round
        self.killed_by = killed_by
        self.remaining_arrows = 0
        
    def __repr__(self):
        # return self.__class__.__name__ + str(self.__dict__)
        print_keys = ('name', 'alive', 'killed_in_round', 'killed_by')
        result = self.__class__.__name__ + '{' 
        result += ', '.join(f'{k}: {self.__dict__[k]}' for k in print_keys)
        result += '}'
        return result

    def killed(self, zombie, round=None):
        if not(self.alive):
            raise RuntimeError(f'Player {self.name} previously killed by {self.killed_by}; cannot be killed again by {zombie}.')
        else:
            self.alive = False
            self.killed_by = zombie
            self.killed_in_round = round

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
    '''
    
    def __init__(self, player, named_zombies, max_rounds=1000, current_round=1, status='Not started'):
        # TODO - add game settings to control 
        self.player = player
        self.zombies = named_zombies
        self.max_rounds = max_rounds
        self.current_round = current_round
        self.status = status

    def __repr__(self):
        '''Display current state of the Game
        '''
        return self.__class__.__name__ + str(self.__dict__)
    
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

        # Advance all live zombies
        for z in self.zombies:
            if z.alive:
                new_dist = z.move()
            if player_lives & (new_dist == 0):
                player_lives = False
                self.player.killed(z, self.current_round)

        if player_lives:
            # Generate new zombies
            print(f'Generating two new zombies ... should be random, but starting with static.')
            for i in range(2):
                self.zombies.append(Zombie.generate_random())

            # Shoot all arrows at most urgent zombies
            self.status = 'Round completed'
            return True
        else:
            self.status = 'Round completed'
            return False

    def prep_next_round(self):
        '''Returns True if player is alive, and preps for next round. Returns False if player is dead.
        '''
        if self.status != 'Round completed':
            raise RuntimeError("Can't prep for next round unless current round is marked completed.")
        
        if not(self.player.alive):
            return False

        if self.current_round == self.max_rounds:
            raise RuntimeError("Can't prep for next round if current round hit the max_rounds.")

        self.current_round += 1
        self.status = 'Not started'
        return True


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

        player = Player('Steve', quiver_capacity = 10)
        
        zombie_inputs = [
            ("Abe", 10, 1, 5), 
            ("Bill", 200, 40, 20),
            ("Chuck", 20, 8, 10)
        ]
        
        game = Game(player = player, named_zombies = [Zombie(*z) for z in zombie_inputs],  max_rounds = 10)
        
        # initial game has no new zombies, no arrows. Ends when Player is eaten.
        player_alive = True
        while (player_alive):
            print(game.summary())
            player_alive = game.play_round()
            game.prep_next_round()
        print(game.summary())


def main():
    Game.TestMe()

if __name__ == '__main__':
    main()


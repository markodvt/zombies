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
        self.arrow_capacity = quiver_capacity
        self.alive = True
        self.entered_in_round = entered_in_round
        self.killed_in_round = killed_in_round
        self.killed_by = killed_by
        
    def __repr__(self):
        # return self.__class__.__name__ + str(self.__dict__)
        print_keys = ('name', 'alive', 'killed_in_round', 'killed_by')
        result = self.__class__.__name__ + '{' 
        result += ', '.join(f'{k}: {self.__dict__[k]}' for k in print_keys)
        result += '}'
        return result

    def killed(self, zombie):
        if not(self.alive):
            raise RuntimeError(f'Player {self.name} previously killed by {self.killed_by}; cannot be killed again by {zombie}.')
        else:
            self.alive = False
            self.killed_by = zombie

class Game:
    '''Game state includes a player (just one for now), a list of named_zombies, a current round (default to 1), and max_rounds (to prevent infinite games).

    Each round of the game:
    - advance the current_round by one
    - player refills their quiver to quiver_capacity
    - all existing (live) zombies advance, in order they entered the game; first one to reach player kills the player
    - new zombies appear at random (non-zero) distances
    - player shoots all arrows, prioritizing zombies closest to player; "closest" is measured as distance/speed (which zombies will reach player soonest) 
    '''
    def __init__(self, player, named_zombies, max_rounds=1000, current_round=1):
        self.player = player
        self.zombies = named_zombies
        self.max_rounds = max_rounds
        self.current_round = current_round
        

    def __repr__(self):
        '''Display current state of the Game
        '''
        return self.__class__.__name__ + str(self.__dict__)

    def pretty_print(self):
        print('\n' + ('=' * 40))
        print('GAME SUMMARY')
        print('=' * 40)
        print('Player ' + self.player.name + ' is: ' + 'ALIVE' if self.player.alive else 'DEAD')
        print('Last round played: ROUND ' + str(self.current_round))        
        print('\nPlayer: ' + str(self.player))
        print('\nZombies:\n')
        for z in self.zombies:
            print(z)
        print('\n\n')

    @classmethod
    def TestMe(cls):

        player = Player('Steve', quiver_capacity = 10)
        
        zombie_inputs = [
            ("Abe", 10, 1, 5), 
            ("Bill", 200, 40, 20),
            ("Chuck", 20, 8, 10)
        ]
        
        game = Game(player = player, named_zombies = [Zombie(*z) for z in zombie_inputs],  max_rounds = 10)
        game.pretty_print()

def main():
    Game.TestMe()

   
if __name__ == '__main__':
    main()


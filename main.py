from zombie import Zombie

'''A Game represewnts the state of a roster of Zombies and the state of the Player over a sequence of rounds.
'''

class Player:
    '''Player has a name and arrow_capacity. 
    TODO - implement strategy later so player can prioritize their arrows.
    TODO - may want to remove 'survived_rounds' later, unless multiple players.
    '''
    def __init__(self, name, arrow_capacity, alive=True, entered_in_round = 1, killed_in_round = None, killed_by = None):
        self.name = name
        self.arrow_capacity = arrow_capacity
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

    def survive_round(self):
        self.survive_round = self.survived_rounds + 1


class Game:
    '''Game state includes a roster of live and dead zombies, a current round, max_rounds, and player
    '''
    def __init__(self, roster, player, max_rounds = 20):
        self.player = player
        self.roster = roster
        self.max_rounds = max_rounds
        self.current_round = 1
        

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
        for z in self.roster:
            print(z)
        print('\n\n')

    @classmethod
    def TestMe(cls):

        player = Player('Steve', arrow_capacity = 10)
        
        zombie_inputs = [
            ("Abe", 10, 1, 5), 
            ("Bill", 200, 40, 20),
            ("Chuck", 20, 8, 10)
        ]
        
        game = Game(roster = [Zombie(*z) for z in zombie_inputs], player = player, max_rounds = 10)
        game.pretty_print()

def main():
    Game.TestMe()

   
if __name__ == '__main__':
    main()


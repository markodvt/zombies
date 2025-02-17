from priority_queue import Priority_queue


class Player:
    '''Player has a name and arrow_capacity. At each round, player reloads arrows.
    '''
    def __init__(self, name, quiver_capacity, zombie_queue=None, alive=True, entered_in_round = 1, killed_in_round = None, killed_by = None):
        self.name = name
        self.quiver_capacity = quiver_capacity
        self.alive = True
        self.entered_in_round = entered_in_round
        self.killed_in_round = killed_in_round
        self.killed_by = killed_by
        self.remaining_arrows = 0
        
    def __repr__(self):
        # return self.__class__.__name__ + str(self.__dict__)
        print_keys = ('name', 'alive', 'quiver_capacity', 'killed_in_round', 'killed_by')
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

import random
from zombie import Zombie

class Zombie_generator:
    '''Random zombie generation function calls
    std::string name  = P2random::getNextZombieName();    	
    uint32_t distance = P2random::getNextZombieDistance();    	
    uint32_t speed    = P2random::getNextZombieSpeed();    	
    uint32_t health   = P2random::getNextZombieHealth();
    '''
    def __init__(self, random_seed, max_rand_distance, max_rand_speed, max_rand_health):
        self.random_seed = random_seed
        self.max_rand_distance = max_rand_distance
        self.max_rand_speed = max_rand_speed
        self.max_rand_health = max_rand_health
        self.Zacks = 0
        random.seed(random_seed)

    def __call__(self):
        '''Class is callable. Generates zombie inputs (in order) using the four helper functions.
        '''
        inputs = {'name': self.getNextZombieName(), 'distance': self.getNextZombieDistance(), 'speed': self.getNextZombieSpeed(), 'health': self.getNextZombieHealth()}    
        return Zombie(**inputs)
    
    def getNextZombieName(self):
        self.Zacks += 1
        return 'Zack' + str(self.Zacks)

    def getNextZombieDistance(self):
        return random.randint(1, self.max_rand_distance)

    def getNextZombieSpeed(self):
        return random.randint(1, self.max_rand_speed)

    def getNextZombieHealth(self):
        return random.randint(1, self.max_rand_health)

    @classmethod
    def TestMe(cls):
        print(f'{'='*40}\nTesting class: {cls.__name__}\n{'='*40}')
        gen1 = Zombie_generator(random_seed=42, max_rand_distance=100, max_rand_speed=30, max_rand_health=10)

        print('Created a generator using this code ...')
        print('Zombie_generator(random_seed=42, max_rand_distance=100, max_rand_speed=30, max_rand_health=10)\n')

        zombie_list1 = [gen1() for i in range(5)]
        print('List of random zombies ....')
        for z in zombie_list1:
            print(z)

        gen2 = Zombie_generator(random_seed=42, max_rand_distance=100, max_rand_speed=30, max_rand_health=10)

        zombie_list2 = [gen2() for i in range(5)]
        print('\nSecond list ... should match first, using same random seed and params ...')
        for z in zombie_list2:
            print(z)

def main():
    Zombie_generator.TestMe()

if __name__ == '__main__':
    main()

class RandomZombieGenerator:
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
    def generate_random_zombie(cls, zombie_generator):
        zombie_input = (
            zombie_generator.getNextZombieName(),
            zombie_generator.getNextZombieDistance(),
            zombie_generator.getNextZombieSpeed(),
            zombie_generator.getNextZombieHealth()
        )
        return Zombie(*zombie_input)

    @classmethod
    def generate_random_Zack(cls):
        '''TODO - make this random. Starting with simple, static constructor.
        '''
        cls.zack_count += 1
        inputs = ('Zack ' + str(cls.zack_count), 100, 10, 50)
        new_zombie = Zombie(*inputs)
        return new_zombie

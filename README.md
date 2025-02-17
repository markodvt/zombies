# Zombies

## Player:
data:
- name
- quiver_capacity
- alive
- entered_round
- killed_in_round
- killed_by

methods:
- killed(zombie, round)


## Zombie:
data:
- name
- distance (to player)
- speed (distace moved per round)
- health (each arrow subs 1 from health)
- round_created
- round_killed
- alive
- ETA (updated as ceil(distance/speed))

methods:
- move (each round, moves "distace")
- suffer_arrows (reduce health, update alive)
- active_rounds (rounds lived so far or until dead)
- priority (returns tuple = (ETA, health, ASCI code of name) since Player shoots zombies according to that order ... )

## Zombie_generator
data:
- random_seed
- max_rand_distance
- max_speed
- max_health

methods:
- constructor configures instance of generator and calls random.seed(random_seed) to initialize
- callable
- helper functions getNextZombieName, etc.

# Main (contains Game Class)
data:
- player
- named_zombies (list)
- zombie_generator
- max_rounds
- current_round
- status

methods:
- generate_random_zombie (calls generator)
- play_round
- prep_next_round
- play_game
- summary (to display game state)

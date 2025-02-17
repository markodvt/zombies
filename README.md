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

## Priority_queue
- push(item, priority)
- pop()
- empty() -> bool

## Main (contains Game Class)
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

## How a Game runs ...

Each round of the game:

- advance the current_round by one
- player refills their quiver to quiver_capacity
- all existing (live) zombies advance, in order they entered the game; first one to reach player kills the player
- new zombies appear at random (non-zero) distances
- player shoots all arrows, prioritizing zombies closest to player; "closest" is measured as distance/speed (which zombies will reach player soonest) 

At each round, move all zombies (even if player had been killed), as verbose mode prints the final positions at end of round, not at death of player.

## Use of priority queue

The game has an attribute zombies = a list of all zombies (living or dead) in the order they were created

In each round, the game's zombies list is updated with new (generated) zombies

After all live zombies advance, a new priority_que is created containing live zombies with their updated ETAs.

The player empties their arrows based on the priority queue.
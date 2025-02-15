from zombie import Zombie

def main():
    print("Run a test game with no arrows ... expect to die.\n\n")
    Zombie.TESTME(arrows_per_zombie=0)

    print("\n\nRun a test game with 10 arrows at each zombie per round ... expect to live.\n\n")
    Zombie.TESTME(arrows_per_zombie=10)

if __name__ == '__main__':
    main()


import random
from goblin import Goblin
from hero import Hero
from boss import IceDragon
from baby_elf import BabyElf

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Kratos")

    # Create goblins
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Create baby elves
    babyelfs = [BabyElf(f"Gorlock the Destroyer {i+1}", "Peach") for i in range(2)] 

    # Create IceDragon boss
    icedragons = [IceDragon(f"Ice Dragon {i+1}", "White") for i in range(1)] 

    # Keep track of stats
    defeated_icedragons = 0
    defeated_goblins = 0
    defeated_babyelfs = 0
    total_damage = 0
    rounds = 0

    # -------------------
    # Battle Loop (Goblins)
    # -------------------
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1

        # Hero's turn
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        if damage > 0:
            print(f"Hero attacks {target_goblin.name} for {damage} damage!")
            target_goblin.take_damage(damage)

            if not target_goblin.is_alive():
                defeated_goblins += 1
                print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                total_damage += damage

    # -------------------
    # Battle Loop (Baby Elves)
    # -------------------
    print("New Opponent Baby Elfs have appeared")      
    while hero.is_alive() and any(babyelf.is_alive() for babyelf in babyelfs):
        print("\nNew Round!")
        rounds += 1

        # Hero's turn
        target_babyelf = random.choice([babyelf for babyelf in babyelfs if babyelf.is_alive()])
        damage = hero.strike()
        if damage > 0:
            print(f"Hero attacks {target_babyelf.name} for {damage} damage!")
            target_babyelf.take_damage(damage)

            if not target_babyelf.is_alive():
                defeated_babyelfs += 1
                print(f"{target_babyelf.name} has been defeated!")

        # Baby Elves' turn
        for babyelf in babyelfs:
            if babyelf.is_alive():
                damage = babyelf.attack()
                print(f"{babyelf.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                total_damage += damage

    # -------------------
    # Goblins & Baby Elves outcome
    # -------------------
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins and baby elves! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # -------------------
    # Boss Battle (IceDragon)
    # -------------------
    defeated_bosses = 0

    if hero.is_alive():
        print("BOSS BATTLE")

    while hero.is_alive() and any(dragon.is_alive() for dragon in icedragons):
        print("\nNew Round!")
        rounds += 1

        # Hero's turn
        damage = hero.strike()
        if damage > 0:
            target_icedragon = random.choice([dragon for dragon in icedragons if dragon.is_alive()])
            print(f"Hero attacks {target_icedragon.name} for {damage} damage!")
            target_icedragon.take_damage(damage)

            if not target_icedragon.is_alive():
                defeated_bosses += 1
                print(f"{target_icedragon.name} has been defeated!")

        # Dragons' turn
        for dragon in icedragons:
            if dragon.is_alive():
                # Freeze only once
                if dragon.health < 175 and hero.frozen == 0 and not dragon.frozen_once:
                    dragon.Freeze(hero)
                # Normal attack if hero is not frozen
                elif hero.is_alive() and dragon.is_alive():
                    damage = dragon.attack()
                    print(f"{dragon.name} attacks hero for {damage} damage!")
                    hero.receive_damage(damage)
                    total_damage += damage

    # -------------------
    # Final Outcome
    # -------------------
    if hero.is_alive():
        print(f"\nThe hero has defeated the Final Boss! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # -------------------
    # Stats
    # -------------------
    print(f"\nTotal damage dealt: {total_damage}")
    print(f"Total rounds fought: {rounds}")
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print(f"\nTotal baby elves defeated: {defeated_babyelfs} / {len(babyelfs)}")
    print(f"\nTotal bosses defeated: {defeated_bosses} / {len(icedragons)}")

if __name__ == "__main__":
    main()

# -------------Scope------------

enemies = 1


def increase_enemies():
    # global var_name enables global variable to be used inside function
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()

# print(potion_strength) is a scope error

# There is no block scope
game_level = 3
enemies = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

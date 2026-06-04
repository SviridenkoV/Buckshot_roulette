import random
from time import sleep


def random_total_bullets():
    min_bullets = 3
    max_bullets = 9
    bullet_count = random.randint(min_bullets, max_bullets)
    return bullet_count

def random_shells(bullet_count):
    bullet_list = []
    for _ in range(bullet_count):
        bullet = random.randint(0, 1)  # 0 = пустой, 1 = боевой
        bullet_list.append(bullet)
    return bullet_list

def type_of_bullet(bullet_list):
    sum_empty_bullet = 0
    sum_battle_bullet = 0
    for bullet in bullet_list:
        if bullet == 0:
            sum_empty_bullet += 1
        else:
            sum_battle_bullet += 1
    return sum_empty_bullet, sum_battle_bullet


def shuffle_bullets(bullet_list):
    shuffled = bullet_list.copy()
    random.shuffle(shuffled)
    return shuffled


def random_hp():
    return random.randint(2, 4)

def shoot_yourself(shuffle_shells, player_hp):
    print("Вы поднесли ружьё к своему рту...")
    sleep(5)
    if shuffle_shells[0] == 0:
        print("Патрон холостой! Вам повезло :)")
        shuffle_shells.pop(0)
        extra_turn = True
        return shuffle_shells, player_hp, extra_turn
    else:
        print("Боевой патрон! Вы потеряли сердце")
        shuffle_shells.pop(0)
        player_hp -= 1
        extra_turn = False
        return shuffle_shells, player_hp, extra_turn

def shoot_enemy(shuffle_shells, enemy_hp):
    print("Вы направили ружьё на диллера...")
    sleep(5)
    if shuffle_shells[0] == 0:
        print("Патрон холостой... Диллер невридим")
        shuffle_shells.pop(0)
        return shuffle_shells, enemy_hp
    else:
        print("Боевой патрон! Диллер потерял 1 сердце!")
        shuffle_shells.pop(0)
        enemy_hp -= 1
        return shuffle_shells, enemy_hp

def diller_turn(shuffle_shells, player_hp):
    if shuffle_shells[0] == 0:
        print("Диллер направил на вас ружьё...")
        sleep(3)
        print("Холостой, вам повезло...")
        shuffle_shells.pop(0)
        return shuffle_shells, player_hp
    else:
        print("Диллер направил на вас ружьё...")
        sleep(5)
        print("Патрон оказался боевым, хуёво")
        shuffle_shells.pop(0)
        player_hp -= 1
        return shuffle_shells, player_hp

total_bullets = random_total_bullets()
shells = random_shells(total_bullets)
empty, live = type_of_bullet(shells)
shuffle_shells = shuffle_bullets(shells)
hero_hp = random_hp()
enemy_hp = random_hp()
empty_bullet, battle_bullet = type_of_bullet(shells)





print(f"Диллер достаёт ружьё...")
sleep(3)
print(f"Всего {total_bullets} пуль...")
sleep(2)
print(f"{empty_bullet} пустых патрона, {battle_bullet} боевых...")
sleep(2)
print("Диллер заряжает ружьё в случайном порядке...")
sleep(2)
print("Игра началась")
print("--------------------------------------------------------")

extra_turn = False

while hero_hp > 0 and enemy_hp > 0:
    print(f"\nВаше здоровье: {hero_hp}, здоровье диллера: {enemy_hp}")
    print(f"Патронов осталось: {len(shuffle_shells)}")
    print("Выстрелить в себя (0) или в диллера (1)?")

    try:
        choice = int(input())
    except ValueError:
        print("Неправильное значение. Выстрелить в себя (0) или в диллера (1)?")
        continue

    if choice == 0:
        shuffle_shells, hero_hp, extra_turn = shoot_yourself(shuffle_shells, hero_hp)
    elif choice == 1:
        shuffle_shells, enemy_hp = shoot_enemy(shuffle_shells, enemy_hp)
        extra_turn = False
    else:
        print("Неправильное значение. Выстрелить в себя (0) или в диллера (1)?")
        continue

    if enemy_hp <= 0:
        print("\n💀 ДИЛЛЕР МЁРТВ 💀")
        print("Вы выжили!")
        break

    if hero_hp <= 0:
        print("\n☠️ ВЫ ПОГИБЛИ ☠️")
        break

    if len(shuffle_shells) == 0:
        print("\nРужьё разряжено! Диллер перезаряжает...")
        sleep(2)
        total_bullets = random_total_bullets()
        shells = random_shells(total_bullets)
        empty, live = type_of_bullet(shells)
        shuffle_shells = shuffle_bullets(shells)
        print(f"Новая обойма: {total_bullets} патронов ({empty} холостых, {live} боевых)")
        sleep(2)

    if not extra_turn:
        print("\nХод диллера...")
        sleep(2)
        shuffle_shells, hero_hp = diller_turn(shuffle_shells, hero_hp)
    else:
        print("\n🔥 ДОПОЛНИТЕЛЬНЫЙ ХОД! 🔥")
        extra_turn = False


    if len(shuffle_shells) == 0:
        print("\nРужьё разряжено! Диллер перезаряжает...")
        sleep(2)
        total_bullets = random_total_bullets()
        shells = random_shells(total_bullets)
        empty, live = type_of_bullet(shells)
        shuffle_shells = shuffle_bullets(shells)
        print(f"Новая обойма: {total_bullets} патронов ({empty} холостых, {live} боевых)")
        sleep(2)





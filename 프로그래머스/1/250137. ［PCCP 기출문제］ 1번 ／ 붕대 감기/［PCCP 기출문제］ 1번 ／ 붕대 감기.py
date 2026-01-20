def solution(bandage, health, attacks):
    max_hp = health
    heal_time, heal_per_sec, bonus_heal = bandage

    time = 0
    combo = 0
    idx = 0

    while idx < len(attacks):
        time += 1

        if time == attacks[idx][0]:
            health -= attacks[idx][1]
            combo = 0
            idx += 1

            if health <= 0:
                return -1
        else:
            combo += 1
            health += heal_per_sec

            if combo == heal_time:
                health += bonus_heal
                combo = 0

            if health > max_hp:
                health = max_hp

    return health

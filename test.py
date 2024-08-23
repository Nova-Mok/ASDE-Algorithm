def can_abhimanyu_cross_chakravyuh(p, a, b, enemy_powers):
    abhimanyu_power = p
    regenerated = [False] * 11

    for i, enemy_power in enumerate(enemy_powers):
        if a > 0:
            a -= 1
            continue

        if abhimanyu_power < enemy_power:
            if b > 0:
                abhimanyu_power = p
                b -= 1
            else:
                return False

        abhimanyu_power -= enemy_power

        if i in (2, 6):
            regenerated[i] = True

        if i > 0 and regenerated[i-1]:
            regen_power = enemy_powers[i-1] // 2
            if abhimanyu_power < regen_power:
                if b > 0:
                    abhimanyu_power = p
                    b -= 1
                else:
                    return False
            abhimanyu_power -= regen_power

    return True

def test_abhimanyu_chakravyuh():
    test_cases = [
        (100, 2, 1, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]),
        (50, 1, 1, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
    ]

    for i, (p, a, b, enemy_powers) in enumerate(test_cases, 1):
        result = can_abhimanyu_cross_chakravyuh(p, a, b, enemy_powers)
        print(f"Test case {i} result: {result}")

if __name__ == "__main__":
    test_abhimanyu_chakravyuh()

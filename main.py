# Dice sum probability calculator
# Författare: Elias Fritioff
# Datum: 2024-08-21

from collections import Counter

def main():
    # Läs in användarens input och dela upp den
    user_input = input().split()
    dice_one = int(user_input[0])
    dice_two = int(user_input[1])

    # Skapa en lista för att hålla alla möjliga summor
    all_sums = []

    # Gå igenom alla möjliga kast för båda tärningarna
    for x in range(1, dice_one + 1):  # Inkludera också högsta värdet
        for i in range(1, dice_two + 1):  # Inkludera också högsta värdet
            all_sums.append(x + i)  # Lägg till summan i listan

    # Använd Counter för att räkna hur ofta varje summa förekommer
    most_common_sums = Counter(all_sums).most_common()

    # Hitta den högsta frekvensen
    max_count = most_common_sums[0][1]

    # Skriv ut alla summor som har maximal sannolikhet
    for sum_val, count in most_common_sums:
        if count == max_count:
            print(sum_val)

# Kör main-funktionen om programmet körs direkt
if __name__ == "__main__":
    main()
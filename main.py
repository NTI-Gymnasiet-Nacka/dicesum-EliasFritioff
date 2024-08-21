# Dice sum probability calculator
# Författare: Elias Fritioff
# Datum: 2024-08-21

from collections import Counter

def main():
    user_input = input().split()
    dice_one = int(user_input[0])
    dice_two = int(user_input[1])
    #sidor på tärningen

    all_sums = [] #listan för summorna

    for x in range(1, dice_one + 1):
        for i in range(1, dice_two + 1):
            all_sums.append(x + i)

    most_common_sums = Counter(all_sums).most_common()
    #counter för att räkna upp alla summor för att senare kunna se hur ofta dom förekommer.

    max_count = most_common_sums[0][1]
    #vi tar reda på den vanligaste förekommande summan

    for sum_val, count in most_common_sums:
        if count == max_count:
            print(sum_val)
    #skriver ut en lista med alla mest förekommande summor.


if __name__ == "__main__":
    main()
#kör main funktionen.
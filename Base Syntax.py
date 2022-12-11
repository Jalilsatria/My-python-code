"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Mom said, "Please go to the market"')
print('Her son said,"Oke, What am I doing in the market?"')
print('Mom said, "Buy 1 bottle of milk, and if they have eggs, bring 6"')
print("Her son goes to the market")
print("and his start shopping")

# Percabangan
The_number_of_milk_bottles = 175
The_number_of_eggs = 1764
print(f"The number of milk bottles is {The_number_of_milk_bottles} bottles ")
print(f"The number of eggs is {The_number_of_eggs} eggs")

if The_number_of_milk_bottles > 0:
    print("His bring enough money to buy mom's wish")
    if The_number_of_eggs == 0:
        print("His buy 1 bottle of milk")
    else:
        print("His buy 1 bottle of milk and 6 eggs")
else:
    print("His didn't buy mom's wish")

print("His back to the home")
print("Her son gives the result to the mom")
print("finish")
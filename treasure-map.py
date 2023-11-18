# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("Welcome to the Treasure Map! Enter a two-digit position (XY) to place the treasure.")
print("Use numbers 1, 2, or 3 for both X (column) and Y (row).")

position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position = list(str(position))

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
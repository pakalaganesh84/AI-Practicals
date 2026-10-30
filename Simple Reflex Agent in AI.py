rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

position = 'A'

while True:

    print("\nCurrent Room:", position)

    if rooms[position] == 'Dirty':

        print("Room is Dirty")
        print("Agent is Cleaning...")

        rooms[position] = 'Clean'

    else:
        print("Room is Already Clean")

    if position == 'A':
        position = 'B'

    else:
        position = 'A'

    if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("\nAll Rooms are Clean!")
        break

print("\nFinal Room Status:", rooms)

A = input(
    "Enter Room A status (Clean/Dirty): "
).capitalize()

B = input(
    "Enter Room B status (Clean/Dirty): "
).capitalize()


position = input(
    "Enter starting position (A/B): "
).upper()


rooms = {
    "A": A,
    "B": B
}


for i in range(4):

    if rooms[position] == "Dirty":

        print(
            "Action: Suck",
            position
        )

        rooms[position] = "Clean"

    else:

        print("Action: Move")

        if position == "A":
            position = "B"
        else:
            position = "A"


print("Final state:", rooms)

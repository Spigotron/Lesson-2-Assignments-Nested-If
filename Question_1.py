place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("Choose an action: climb a tree or cross a river?")
    if action == "climb a tree":
        print("You find a bird's nest!")
    elif action == "cross a river":
        print("You find a boat!")
    else:
        pass
elif place == "cave":
    action = input("Choose an action: light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Your torchlight gleams off crystalline walls. What treasures lie in wait in this mystical place?")
    elif action == "proceed in the dark":
        print("You confidently stride forward into the blackness and promptly fall to your death in a deep chasm. Game over, man!")
    else:
        pass
else:
    pass
attendees = int(input("Enter number of attendees: "))
food = input("Do you want vegetarian food?")
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "large speakers" if attendees > 100 else "small speakers"
projector = "large projector" if attendees > 100 else "small projector"
if food == "yes":
    print("We recommend 'Veggie Delight Caterers.'")
else:
    print("We recommend 'Gourmet Meals Caterers.'")
print(venue)
print(audio_system)
print(projector)
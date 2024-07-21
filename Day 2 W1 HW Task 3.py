attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(f"Venue: {venue}")

food_preference = input("Do you want vegetarian food? (yes/no): ").lower()
caterer = "Veggie Delight Caterers" if food_preference == "yes" else "Gourmet Meals Caterers"
print(f"Recommended Caterer: {caterer}")

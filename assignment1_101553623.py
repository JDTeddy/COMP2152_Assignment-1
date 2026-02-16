"""
Author: <Jared-Ian Duldulao>
Assignment: #1
"""

# Step b: Create 4 variables
Gym_member = "Junn Halllond"

preferred_weight_kg = 80

highest_reps = 40

membership_active = True

# Step c: Create a dictionary named workout_stats

# Workout stats are based on minutes in (Yoga, Running, Weightlifting)
workout_stats = {
    "Junn": (25, 60, 45),
    "Arthur": (30, 40, 50), 
    "Lynn": (40, 50, 20)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
workout_list = [list(workout_stats[friend]) for friend in workout_stats if "_Total" not in friend]

# Step f: Slice the workout_list
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for friend in workout_stats:
    if "_Total" in friend:
        if workout_stats[friend] >= 120:
            name = friend.replace("_Total", "")
            print(f"\nGreat job being active, {name}!")

# Step h: User input to look up a friend
search_name = input("Enter a friend's name: ")

if search_name in workout_stats:
    minutes = workout_stats[search_name]
    total = workout_stats.get(search_name + "_Total")
    print(f"{search_name}'s workout minutes:")
    print(f"Yoga: {minutes[0]} minutes")
    print(f"Running: {minutes[1]} minutes")
    print(f"Weightlifting: {minutes[2]} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"Friend {search_name} not found in records")

# Step i: Friend with highest and lowest total workout minutes
totals_only = {friend.replace("_Total", ""): workout_stats[friend]
               for friend in workout_stats if "_Total" in friend}

highest_friend = max(totals_only, key=totals_only.get)
lowest_friend = min(totals_only, key=totals_only.get)

print("Friend with the highest total of workout minutes: ", highest_friend)
print("Friend with the lowest total of workout minutes: ", lowest_friend)
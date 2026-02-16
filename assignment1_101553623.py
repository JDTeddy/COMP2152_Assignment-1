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
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[friend + "_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
workout_list = [list(minutes) for friend, minutes in workout_stats.items() if not friend.endswith("_Total")]

# Step f: Slice the workout_list
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for friend in workout_stats:
    if friend.endswith("_Total") and workout_stats[friend] >= 120:
        friend_name = friend.replace("_Total", "")
        print(f"Great job with being active, {friend_name}!")

# Step h: User input to look up a friend
search_name = input("Enter a friend's name: ")

if search_name in workout_stats and not search_name.endswith("_Total"):
    activities = workout_stats[search_name]
    total = workout_stats[search_name + "_Total"]
    print(f"{search_name}'s workout minutes:")
    print(f"Yoga: {activities[0]} minutes")
    print(f"Running: {activities[1]} minutes")
    print(f"Weightlifting: {activities[2]} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"Friend {search_name} not found in records")

# Step i: Friend with highest and lowest total workout minutes
totals = {friend.replace("_Total", ""): minutes
          for friend, minutes in workout_stats.items()
            if friend.endswith("_Total")
         }

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("Friend with the highest total of workout minutes: ", highest_friend)
print("Friend with the lowest total of workout minutes: ", lowest_friend)
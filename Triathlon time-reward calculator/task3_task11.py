import math # Imports math function into this python file

# Requests user input for the following race times as an integer, (float will allow for decimals to be added)
time_swimming = float(input("Please input your swimming time in minutes: "))
time_cycling = float(input("Please input your cycling time in minutes: "))
time_running = float(input("Please input your running time in minutes: "))

# Adds the 3 race time together and is assigned to new variable for the total race time, prints result
total_triathlon_time = time_swimming + time_cycling + time_running
print(f'Your total time for the triathlon is {total_triathlon_time} minutes')

# Variables assigned with reward options for within certain race bench mark times
_100_qualifying_time = "Provincial colours!"
_105_qualifying_time = "Provincial half colours!"
_110_qualifying_time = "Provincial scroll!"
_gt_110_qualifying_time = "No reward!"

# Condition to check if total is either: Less than 100, between 100 and 105, between 105 and 110 or greater than 110
# Will tell the player what reward they get based on their total time calculation for all 3 races.
if total_triathlon_time <= 100:
    print(f'You have earned {_100_qualifying_time}')
elif total_triathlon_time > 100 and total_triathlon_time <= 105:
    print(f'You have earned {_105_qualifying_time}')
elif total_triathlon_time > 105 and total_triathlon_time <= 110:
    print(f'You have earned {_110_qualifying_time}')
elif total_triathlon_time > 110:
    print(f'You have earned {_gt_110_qualifying_time}')

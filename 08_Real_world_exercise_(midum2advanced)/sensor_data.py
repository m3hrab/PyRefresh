"""### Exercise 5: **Sensor Data Collection**
You are working with data collected from temperature sensors over a week. Each sensor records the temperature once a day. Write a function to:
- Find the highest and lowest temperature recorded.
- Find the average temperature for the week.
"""

sensor_data = [
    (72, 68, 70, 71, 69, 74, 73),  # Sensor 1
    (67, 65, 69, 72, 66, 70, 68),  # Sensor 2
]

both_sensor_data = sensor_data[0] + sensor_data[1]

print(f"Highest temperature recorded: {max(both_sensor_data)}°F")
print(f"Lowest temperature recorded: {min(both_sensor_data)}°F")
print(f"Average temperature for the week: {sum(both_sensor_data)/len(both_sensor_data):.1f}°F")



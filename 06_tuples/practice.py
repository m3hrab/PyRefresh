"""
    Task: You have a list of cities and their respective GPS coordinates stored in tuples. Write a function that takes the name of a city as input and returns its GPS coordinates.
"""
cities = [("New York", (40.7128, 74.0060)), 
          ("London", (51.5074, -0.1278)), 
          ("Tokyo", (35.6762, 139.6503))]

def get_coordinates(city_name):
    # Your code here
    for city in cities:
        if city_name == city[0]:
            return city[1]
        

print(get_coordinates("Tokyo"))

"""Task: You have employee data stored as tuples in the form (ID, Name, Role, Salary). Write a function that takes the employee's ID and returns their name and role."""

employees = [(1, "Alice", "Engineer", 75000), 
             (2, "Bob", "Designer", 68000), 
             (3, "Charlie", "Manager", 90000)]

def get_employee_details(employee_id):
    # Your code here
    for employee in employees:
        if employee[0] == employee_id:
            return employee[1:3]
        
print(get_employee_details(1)) 


"""Task: You are working with RGB colors. Write a function that takes a color tuple (R, G, B) and returns the name of the color based on predefined tuples for basic colors.
"""
basic_colors = {"Red": (255, 0, 0), "Green": (0, 255,0), "Blue": (0, 0, 255)}

def identify_color(color_tuple):
    # Your code here
    for color,rgb in basic_colors.items():
        if rgb == color_tuple:
            return color
        
print(identify_color((255, 0,0)))

"""
Task: You are managing flight schedules. Write a function that takes a pair of cities (e.g., "NYC" and "LAX") and returns the scheduled flight time.
"""
flight_schedule = {("NYC", "LAX"): "10:30 AM", ("LAX", "SF"): "12:00 PM", ("NYC", "Chicago"): "3:45 PM"}

def get_flight_time(departure, destination):
    # Your code here
    temp = (departure, destination)
    for cities, time in flight_schedule.items():
        if cities == temp:
            return time 
        
print(get_flight_time("NYC", "LAX"))
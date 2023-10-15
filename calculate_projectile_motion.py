# Program of the Day: Projectile Motion Calculator

import math

def calculate_projectile_motion(initial_velocity, launch_angle, gravity):
    # Convert launch angle to radians
    launch_angle_rad = math.radians(launch_angle)
    
    # Calculate time of flight
    time_of_flight = (2 * initial_velocity * math.sin(launch_angle_rad)) / gravity
    
    # Calculate maximum height
    max_height = (initial_velocity**2 * (math.sin(launch_angle_rad)**2)) / (2 * gravity)
    
    # Calculate horizontal range
    horizontal_range = (initial_velocity**2 * math.sin(2 * launch_angle_rad)) / gravity
    
    return time_of_flight, max_height, horizontal_range

# Example usage: Calculate projectile motion
initial_velocity = 20.0  # Initial velocity in meters per second
launch_angle = 45.0  # Launch angle in degrees
gravity = 9.81  # Acceleration due to gravity in m/s^2

time, height, range = calculate_projectile_motion(initial_velocity, launch_angle, gravity)
print(f"Time of Flight: {time} seconds")
print(f"Maximum Height: {height} meters")
print(f"Horizontal Range: {range} meters")

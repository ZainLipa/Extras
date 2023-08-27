# Program of the Day: Monte Carlo Simulation for Pi Calculation

import random

def monte_carlo_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2

        if distance <= 1:
            inside_circle += 1

    return (inside_circle / num_points) * 4

# Example usage
num_points = 100000
approx_pi = monte_carlo_pi(num_points)
print("Approximate value of Pi using Monte Carlo Simulation:", approx_pi)

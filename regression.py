#!/usr/bin/env python
# coding: utf-8

# # Project: Linear Regression

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

# Calculate the value of the regression line 'y'

def get_y(m, b, x):
    y = m * x + b
    return y

# Calculates the error ( distance ) of each point (pair) in the data set

def calculate_error(m, b, point):
    x_point, y_point = point
    y = m * x_point + b
    distance = abs(y - y_point)
    return distance

# Calculates the error for each pair in the data set by invoking the 'calculate_error(m, b, point)' function

def calculate_all_error(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        error = calculate_error(m, b, point)
        total_error += error
    return total_error


# Try multiple slopes ( values for m ), and intercepts ( values for b) in increments of 0.1 within range ( -100,100) for m, and (-20, 20) for b

possible_m = [m * 0.1 for m in range(-100, 100)]
possible_b = [b * 0.1 for b in range(-20, 20)]

# Identify the value of the best 'm' and best 'n' to be used with the data set in order to get the most accurate bounciness prediction

smallest_error = float('inf')  # so that error < smallest_error True
best_m = 0
best_b = 0

for m in possible_m:
    for b in possible_b:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print('Best m:', best_m, 'Best b:', best_b, 'Smallest error:', smallest_error)

print('Ball bounces', get_y(0.3, 1.7, 6), 'meters') # For a 6 cm ball the Linear Regression predicts a bounciness of 3.5 meters.

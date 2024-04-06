# given array [0,2,2,4,5,1,0] and the starting point 3, bob can travel at most 1 step by going 4 to 2 ,
# in the next step he cannot go 2 to 2 because he can only go downhill. 
def farthest_distance(values, starting_point):
    current_index = starting_point
    max_steps = 1  # Bob can travel at most 1 step
    steps_taken = 0

    while steps_taken < max_steps:
        # Check if the current index is within the bounds of the array
        if current_index >= 0 and current_index < len(values):
            # Get the value at the current index
            current_value = values[current_index]

            # Check if the next index is within the bounds of the array
            if current_index + current_value >= 0 and current_index + current_value < len(values):
                next_value = values[current_index + current_value]

                # Check if Bob can only go downhill
                if next_value < current_value:
                    # Update the current index to the next index
                    current_index = current_index + current_value
                    steps_taken += 1
                    max_steps = max(steps_taken, max_steps)  # Update max_steps

                else:
                    break  # Bob cannot go uphill, so stop

            else:
                break  # Next index is out of bounds, so stop

        else:
            break  # Current index is out of bounds, so stop

    return current_index

# Test the function with the given array and starting point
values = [0, 2, 2, 4, 5, 1, 0]
starting_point = 6
result = farthest_distance(values, starting_point)
print("Farthest reachable index:", result)

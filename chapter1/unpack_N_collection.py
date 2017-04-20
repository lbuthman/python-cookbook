# Star Expression to unpack unknown number of variables

# temperature tuple
temps = (75, 68.9, 73, 55, 58,3, 60, 77)

# find the average of the previous days compared to current day
*past_temps, today_temp = temps

# calculate average of previous days
past_average = sum(past_temps) / len(past_temps)

print(past_average)

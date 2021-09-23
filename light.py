# prompt user for an object's distance in miles
distance = float(input("Enter astronomical object's distance [mi]:\n"))

# convert miles to meters
meters = (distance / .000621)

# determine the amount of seconds of light travel time for the distance
totalseconds = (meters / 299792458)

# convert totalseconds into full hours, with a remainder of minutes and seconds
hours = totalseconds // (60 * 60)

# convert totalseconds into full minutes by subracting the full hours with a remainder of seconds
mins = (totalseconds - (hours * 60 * 60)) // 60

# determine the final amount of seconds by subtracting the full hours and full minutes
true_secs = (totalseconds - (hours * 60 * 60) - (mins * 60))

# tell the user the light travel time in full hours, full minutes, and fractioned seconds
print("Light travel time:" , hours , "h" , mins , "m {:.1f}" .format(true_secs) , "s" , sep = " ")

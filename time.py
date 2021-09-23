# prompt the user for an amount of seconds
wanted_sec = int(input("Please enter the number of seconds:\n"))

# convert the seconds into whole minutes, leaving a remainder of seconds
mins = int(wanted_sec // 60)

# convert the minutes into whole hours, leaving another remainder of minutes
hours = int(mins // 60)

# determine the number of minutes by subtracting the amount of whole hours from the total time
true_mins = int((wanted_sec / 60) - (hours * 60))

# determine the number of seconds by subtracting the amount of whole minutes that remain from the whole hours from the total time
true_secs = int((wanted_sec - (hours * 60 * 60)) - (true_mins * 60))

# tell the user how many hours, minutes, and seconds make up the amount of seconds they gave
print(wanted_sec , "seconds=" , hours , "hours," , true_mins , "minutes, and" , true_secs , "seconds.")

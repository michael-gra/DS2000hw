# prompt the user for required information
km = float(input("Enter distance of run (km):\n"))
mins = int(input("Enter time of run (minutes):\n"))
secs = int(input("Enter time of run (seconds):\n"))

# convert kilometers to miles
# float is necessary to include the strings of decimals
miles = float(km * .621)

# determine the total amount of full seconds
totalsecs = int((mins * 60) + secs)

# determine number of seconds ran per mile
# float is necessary to include the strings of decimals
pace_seconds = float(totalsecs / miles)

# determine the number of whole minutes ran per mile
pace_mins = float((pace_seconds // 60))

# determine the number of seconds remaining after whole minutes per mile
final_seconds = float((pace_seconds - (pace_mins * 60)))

# tell the user the full number of miles
print("Your pace was " , pace_mins , " minutes and {:.1f}" .format(final_seconds) , "seconds per mile." , sep = "")

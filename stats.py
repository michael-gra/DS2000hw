#DS2000 Grace Michael

# for Values
integers = input("Enter a sorted list of intergers each in the range (0-99):\n").split(' ')
print("Values: " , len(integers))

#variables
summ = 0.0
mean = 0.0
median = 0.0
mode = 0.0
numbers = len(integers)

# for Mean
for n in integers:
    summ += float(n)
mean = summ / numbers
print("Mean: " , mean)

# for Median

if len(integers) % 2 == 0:
   median1 = float(integers[len(integers) // 2])
   median2 = float(integers[len(integers) // 2 - 1])
   median = (median1 + median2) / 2
else:
   median = integers[len(integers) // 2]
print("Median: " , median)

# for Mode
counter = 0
num = integers[0]
# loop for frequency of each number
for i in integers:
    curr_frequency = integers.count(i)
    if(curr_frequency > counter):
        # curr_frequency becomes the counter if larger than other counters
        counter = curr_frequency
        # defines largest frequncy as mode
        num = i
print("Mode: " , num)

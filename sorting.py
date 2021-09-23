# DS2000 Grace Michael

sequence = input("Enter digit sequence:\n")
sequence2 = list(sequence)
sorted = []
# create loop since no set sequence number
while sequence2:
    minimum = sequence2[0]
    for x in sequence2:
        if x < minimum:
            minimum = x # makes smallest values first
    # return the list into sorted sequence
    sorted.append(minimum)
    sequence2.remove(minimum)
print(''.join(sorted))

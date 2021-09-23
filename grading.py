# DS2000 Grace Michael

totalweight = input("Enter grade weights:\n").split(' ')
gradeweight = 0.0

# loop for grade weights
for weight1 in totalweight:
    scoreslst = input("Enter grades (" + weight1 + "%):\n").split(' ')
    number = len(scoreslst) # number of grades in each weight
    summ = 0.0
    #loop for grade scores
    for n in scoreslst:
        summ += float(n)
    average = summ / number
    gradeweight += (summ * float(weight1)) / (100 * number)
print("Course grade: " , round(gradeweight))

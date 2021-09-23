# Grace Michael
# DS2000 Sec 01

# Returns the absolute value
# of the supplied value
# Input: number
# Output: number
def myabs(input):
    if input <= 0:
        # negative times a negative is positve
        return input * -1
    else:
        return input * 1

# Returns the taxi-cab distance
# between the supplied list of coordinates
# Input: two lists of numbers (assumed same length)
# Output: number
# same as myabs but format matches better
def abs_difference(x , y):
    if x > y:
        return (x - y)
    else:
        return (y - x)

def mymanhattan(x1 , y1):
    dimension = len(x1)
    distance = 0
    for dim in range(dimension):
        # sum of all absolute differences
        distance += abs_difference(x1[dim] , y1[dim])
    return distance

# Returns the number of positions that have
# different values in the supplied
# list of coordinates
# Input: two lists of numbers (assumed same length)
# Output: number
def myhamming (p1, p2):
    ham = 0
    L = len(p1)
    for i in range(L):
        # if coordinate points don't match between lists
        # add one to hamming
        if p1[i] != p2[i]:
            ham += 1
    return ham

# Returns the straight-line distance
# between the supplied list of coordinates
# Input: two lists of numbers (assumed same length)
# Output: number
def myeuclidean(x2 , y2):
    dimension = len(x2)
    squaredistance = 0
    sumdistance = 0
    sqrtdistance = 0
    for dim in range(dimension):
        squaredistance = (abs_difference(x2[dim] , y2[dim])) ** 2
        sumdistance += squaredistance
        sqrtdistance = sumdistance ** (1/2)
    return sqrtdistance

# Returns the label of the item in the
# "community" that is closest
# to the search point ("p") according
# to the distance function ("df")
# Input:
    #   p = [coordinates]
    #   community = [["label", [coordinates]],]
    #   df = function([coordinates], [coordinates]) -> number

def nearestneighbor(p , community , df):
    # access the coordinates
    smallestdistance = df(p , community[0][1])
    # access the labels
    smallestlabel = community[0][0]
    for i in range(len(community)):
        totaldistance = df(p , community[i][1])
        # determine smallest distance
        if(smallestdistance > totaldistance):
            smallestdistance = totaldistance
            # we want the label of the smallest distance
            smallestlabel = community[i][0]
    return smallestlabel

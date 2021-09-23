"""
Grace Michael
DS2000: Programming with Data
HW 6
"""

# Q1 - 10 points
def read_words(filename, ignore='#'):
    # open file to read
    with open(filename, 'r') as file:
        lines = file.readlines()
        # take out ignore character and blanks
        words = [line[:-1] for line in lines if line.startswith('#') == False and line != '\n']
    return words

# Q2 - 10 points
def read_json(filename):
    # importing the module
    import json
    # opening JSON file
    with open(filename) as scoring:
       #return(json.load(scoring))
       my_data = json.load(scoring)
    return my_data

# Q3 - 10 points
def score_word(word, letter_values):
    word_score = 0
    #match style to scoring.json
    letters = list(word.upper())
    for characters in letters:
        if characters in letter_values:
            # if letters in word in data, add to the score
            word_score = word_score + letter_values[characters]
        if characters not in letter_values:
            # give default score if not in the data
            word_score = word_score + letter_values['default']
    return word_score

# Q4 - 10  points
def reverse(word):
    if len(word) == 0:
        return word
    else:
        # move characters from start of string to end
        return reverse (word[1:]) + word[0]

# Q5 - 10 points
def highest_scoring_palindrome(words, letter_values):
    max_score = 0
    max_word = ''
    for word in words:
        # check if palindrome and get score
        if word == reverse(word) and score_word(word, letter_values) > max_score:
            max_score = score_word(word, letter_values)
            # get corresponding word for score
            max_word = word
    return (max_word, max_score)

# Q6 - 10 points
def highest_score_difference(words, values1, values2):
    difference = 0
    diff_word = ''
    for scores in words:
        # use score_words to find scores, subtract for differnce
        if score_word(scores, values1) - score_word(scores, values2) >= difference:
            # make the difference not negative
            difference = abs(score_word(scores, values1) - score_word(scores, values2))
            # return the word in relation to the score
            diff_word = scores
    return (diff_word, difference)

# Q7 - 40 points
def analyze(filename, columns=[], precision=1):

    import csv

    with open(filename, 'r') as file:
        # seperate with commas
        file_read = csv.reader(file, delimiter=',')
        # turn file into list
        row_list = list(file_read)
        # ignore data labels
        del row_list[0]

    stats_dict = {}
    for name in columns:
        value_dict = {"min" : 0, "max" : 0, "avg" : 0}
        # create dict in dict
        stats_dict[name] = value_dict
    # skip data labels, include all other columns
    for x in range(1 , len(columns) + 1):
        # empty list to store values for column
        save = []
        for row in row_list:
            # add the column values to that list
            save.append(float(row[x]))

        stats_dict[(columns[x-1])][("min")] = min(save)
        stats_dict[(columns[x-1])][("max")] = max(save)
        stats_dict[(columns[x-1])][("avg")] = sum(save) / float(len(save))

    # give table labels
    print("\tmin\tavg\tmax")
    for name in columns:
        stats_dict[name]['min']
        stats_dict[name]['max']
        stats_dict[name]['avg']
        # print organized table
        print(name + '\t' + str(stats_dict[name]['min']) + '\t' + str(round(stats_dict[name]['avg'], precision)) + '\t' + str(stats_dict[name]['max']))


# Don't change this function
def main():

    words = read_words('words.txt')
    print(len(words),"words read from",words[0], "to", words[-1])

    scoring = read_json('scoring.json')
    print('Scoring methods: ', ", ".join(scoring.keys()))

    print("\n\nPALINDROMES")
    for method in scoring.keys():
        print(f"Best palindrome ({method}): ", highest_scoring_palindrome(words, scoring[method]))

    print("\n\nPOINT DIFFERENCES")
    print("Biggest point difference (Scrabble > WWF): ", highest_score_difference(words, scoring['scrabble'], scoring['words_with_friends']))
    print("Biggest point difference (WWF > Scrabble): ", highest_score_difference(words, scoring['words_with_friends'], scoring['scrabble']))

    print("\n\n\nANALYZING GRADES")
    print(analyze('grades.csv', ['test1', 'test2', 'test3', 'test4']))


# Don't change these two lines
if __name__ == '__main__':
    main()


"""
	min	avg	max
test1	80.5	93.9	100.0
test2	67.0	87.9	98.0
test3	68.0	90.8	100.0
test4	80.0	94.2	100.0
"""

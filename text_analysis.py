"""
Grace Michael
DS2000: Programming with data
HW 5
text_analysis.py
"""

def count_character(text, char):
    count = 0
    for i in text:
        #if the character in text is the input character
        if i == char:
            count = count + 1
    return count

def count_sentences(text):
    count_sent = 0
    for x in text:
        #if the character is a period, then it is a sentence
        if x == '.':
            count_sent = count_sent + 1
    return count_sent


def text_to_words(text, punctuation = ".,?;-"):
    # change '\n' to spaces
    clean = text.replace('\n', ' ')
    # split string with spaces into seperate words
    for punct in punctuation:
        clean = clean.replace(punct, '')
    return clean.split(" ")

def count_words(text):
    words = 0
    list = text_to_words(text, punctuation = ".,?;-")
    # count the number of words in the list
    for words in list:
        words = len(list)
    return words


def words_per_sentence(text):
    for word in text:
        # number of words / number of sentences
        average = (((count_words(text))) / float(count_sentences(text)))
    return average


def word_count(text, punctuation=".,?;-"):
    dct = {}
    edit_text = text_to_words(text, punctuation = ".,?;-")
    for word in edit_text:
        if word in dct:
            # if word in text, add to frequency count in dict
            dct[word] += 1
        else:
            #if not, don't add anything
            dct[word] = 1
    return dct


def big_words(text, min_length=10):
    list = text_to_words(text, punctuation=".,?;-")
    big_list = []
    for words in list:
        #if the length of the word is >= 10, add them to the empty list
        if len(words) >= 10:
            big_list.append(words)
    #return the empty list full of big words
    return big_list


def common_words(text, min_frequency=10):
    dict_com = word_count(text, punctuation=".,?;-")
    count = 0
    count_word = ''
    for key, value in dict_com.items():
        #if the word count >= 10, the count is their value (in dict)
        if value >= 10:
            count = value
            count_word = key
    return (count_word, count)


def most_common_big_word(text, min_word_size=5):
    dict = word_count(text, punctuation=".,?;-")
    max = 0
    max_word = ''
    for key, value in dict.items():
        #finds highest frequency of words > 5 letters long
        if value > max and len(key) > 5:
            max = value
            max_word = key

    return (max_word, max)


def avg_word_length(text):
    words = text_to_words(text, punctuation=".,?;-")
    count = 0
    for i in words:
        #count the characters of the words
        for j in i:
            count = count + 1
    g = len(words)
    average = count / g
    return average


# %% DON'T CHANGE BELOW THIS LINE!!


def text_analysis(text):
    """ DO NOT CHANGE THIS: Analyze some text and print some statistics """
    print("sentences             :", count_sentences(text))
    print("words                 :", count_words(text))
    print("word/sentence         :", round(words_per_sentence(text), 2))
    print("common (freq >= 10)   :", common_words(text, 10))
    print("big (len >= 11)       :", big_words(text, 11))
    print("common big (len >= 9) :", most_common_big_word(text, 9))
    print("avg word length       :", round(avg_word_length(text), 2))


gettysburg_address = """
Four score and seven years ago our fathers brought forth
on this continent, a new nation, conceived in Liberty,
and dedicated to the proposition that all men are created
equal. Now we are engaged in a great civil war, testing
whether that nation, or any nation so conceived and so
dedicated, can long endure. We are met on a great
battlefield of that war. We have come to dedicate a
portion of that field, as a final resting place for
those who here gave their lives that that nation might
live. It is altogether fitting and proper that we should
do this. But, in a larger sense, we can not dedicate, we
can not consecrate, we can not hallow this ground.
The brave men, living and dead, who struggled here,
have consecrated it, far above our poor power to add
or detract. The world will little note, nor long
remember what we say here, but it can never forget what
they did here. It is for us the living, rather, to be
dedicated here to the unfinished work which they who
fought here have thus far so nobly advanced. It is
rather for us to be here dedicated to the great task
remaining before us—that from these honored dead we
take increased devotion to that cause for which they
gave the last full measure of devotion that we here
highly resolve that these dead shall not have died in
vain that this nation, under God, shall have a new
birth of freedom and that government of the people, by
the people, for the people, shall not perish from the
earth.
"""

text_analysis(gettysburg_address)

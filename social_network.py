"""
Grace Michael
DS2000: Programming with Data
HW 9:
SocialNetwork.py: A class for social networks,
    keeping track of who is friends with who

    I recommend you start by drawing the social network depicted by the data contained
    in friends.txt

    """
class SocialNetwork:
    """ This class represents people knowing other people """

    def __init__(self):
        self.network = {}
        """ Create an empty social network """


    def read_network(self, filename):
        with open(filename, 'r') as f:
            # seperate file into lines
            for line in f.readlines():
                # specify key, value
                (name1, name2) = line[:-1].split(',')
                # make the network
                self.register(name1)
                self.register(name2)
                self.friend(name1, name2)


        """ Read data containing friend pairs.
            With each line, call the friend method: self.friend(name1, name2) """


    def register(self, name):
        # add people to network
        if name not in self.network:
            # use a set as value
            self.network[name] = set()
        return self.network
        """ Add a person with no friends into the network.
            Do nothing if the person is already in the network """


    def friend(self, name1, name2):
        # add mutual friendships to set
        self.network[name1].add(name2)
        self.network[name2].add(name1)

        """ Add two people as mutual friends. Do nothing if they
        are already mutual friends """


    def unfriend(self, name1, name2):
        # remove mutual friendships from set
        self.network[name1].remove(name2)
        self.network[name2].remove(name1)

        """ Make two people no longer friends. """


    def get_friends(self, name):
        # return the value set for a name
        return self.network.get(name)
        """ Return all of name's friends """


    def describe(self):
        print("NETWORK SUMMARY")
        # length of number of keys
        number_in = len(self.network.keys())
        print('There are', number_in , 'people in the network.')
        # determine the total number of connections between friends
        total_values = 0
        no_friends = 0
        longest = 0
        longest_name = ''
        for person in self.network:
            total_values = total_values + len(self.network[person])
            # longest list of connections is the most friends
            if len(self.network[person]) >= longest:
                longest = len(self.network[person])
                # name of person
                longest_name = person
            # if no friends
            if len(self.network[person]) == 0:
                no_friends = no_friends + 1
        average =  total_values / number_in
        print('There is an average of', average ,'friends per person.')
        print('There are', no_friends , 'people with no friends.')
        print('The friendliest person is', longest_name ,'with', longest ,'friends.' )

        """ Generate a report:
            - # people are in our network?
            - # friends per person
            - # number of people with no friends
            - The friendliest person and number of friends """



    def recommend(self, name):
        new_friends = []
        # name's list of friends
        friends = self.get_friends(name)
        for names in friends:
            # list of names's (from name) friends
            friends_2 = self.get_friends(names)
            for second_friends in friends_2:
                # double check they aren't friends with friends
                more_friends = self.get_friends(second_friends)
                # if name not in friends friends and not a friend and friends friend not already in list
                if name not in more_friends and name != second_friends and second_friends not in new_friends:
                    new_friends.append(second_friends)

        return new_friends


        """ Return everyone who is a friend of all of name's friends
            who aren't already friends with name.  Only recommend
            each friend once. """



def main():

    # Create an empty network
    net = SocialNetwork()

    # Read the network
    net.read_network('friends.txt')

    # Based on the current social network, who should Monica be friends with?
    print(net.recommend('Monica'))

    # Monica decides to unfriend John.
    net.unfriend('Monica', 'John')

    # Now recommend new friends for monica
    print(net.recommend('Monica'))

    # Joe is new to our network but has no friends
    net.register('Joe')

    # Who else can we recommend for Joe?
    print(net.recommend('Joe'))

    # Network stats
    net.describe()




if __name__ == "__main__":
    main()

# OUTPUT
'''
['Laney']
['John', 'Laney']
[]
NETWORK SUMMARY
There are 10 people in the network.
There is an average of 2.2 friends per person.
There are 1 people with no friends.
The friendliest person is Laney with 6 friends.
'''

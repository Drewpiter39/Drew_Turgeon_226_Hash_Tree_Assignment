class DataItem:
    def __init__(self, line):
        # Attrubutes of each movie/line
        self.movieName = line[0] # Name
        self.genre = line[1] # Genre
        self.releaseDate = line[2] # Date
        self.director = line[3] # Director
        self.revenue = line[4] # Money
        self.rating = line[5] # Score
        self.minDuration = line[6] # Length
        self.productionCompany = line[7] # Company
        self.quote = line[8] # Quote

# Turns the the string into its unicode variant
def hashFunction(stringData):
    # Do things to stringData, turn into an int
    # The thing that stores the turn
    turn = 0
    # For each character in the string it will cycle
    for char in stringData:
        # Adds the unicode to turn
        turn = (turn + ord(char))
    # Returns the unicode variant
    return turn




import csv
size = 10000
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"
counter = 0

with open(file, 'r', newline = '', encoding = "utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # newItem = DataItem(row)

        # print(row[0])
        print(hashFunction(row[0]))

        # Create a DataItem from row
        # feed the appropriate field into the hash function
        # to get a key
        # mod the key value by the hash table length
        # try to insert DataItem into hash table
        # handle any collisions
        counter += 1
print(counter)

# import random

# def createList(n): # creates a random list of size n
#     x = []
#     for i in range(n):
#         x.append(random.randint(1, 10000))
#     return x
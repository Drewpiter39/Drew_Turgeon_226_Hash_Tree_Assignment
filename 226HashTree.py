class DataItem:
    def __init__(self, line):
        # self.movieName
        #self.genre
        # self.releaseDate
        # self.director
        # self.revenue
        # self.rating
        # self.minDuration
        # self.productionCompany
        # self.quote
        pass 

def hashFunction(stringData):
    # Do things to stringData, turn into an int
    pass

import csv
size = 10000
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"
counter = 0

with open(file, 'r', newline = '', encoding = "utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        newItem = DataItem(row)

        print(row)
        # Create a DataItem from row
        # feed the appropriate field into the hash function
        # to get a key
        # mod the key value by the hash table length
        # try to insert DataItem into hash table
        # handle any collisions
        counter += 1
print(counter)
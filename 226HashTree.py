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
        turn += ord(char)
    # Returns the unicode variant
    return turn

def quadProbing(table, key, movie):
    # The index that is being searched for collision 
    # Modulus len(table) keeps it within valid space
    index = key % len(table)
    # counts to collisions to find empty spot
    collision = 0

    # Tracks positioning for equation
    i = 0

    # So long as the table index that you are looking at is occupied
    while table[index] != None:
        # Adds one to collision
        collision += 1
        # Adds one to location counter
        i += 1
        # Checks to see if i has gotten to large and exits
        if i >= len(table):
            return collision
        # Calculates new spot 
        index = (key + (i * i)) % len(table)

    # Sets the free spot equal to the dataItem that you are adding
    table[index] = movie
    # Returns the collison amount
    return collision

# Imports time so that we can track how long each function takes
import time

# Imports csv to read file
import csv
size =  15001 # Sets size 
hashTitleTable = [None] * size # Creates the hash table for titles
hashQuoteTable = [None] * size # Creates the hash table for quotes

file = "MOCK_DATA.csv" # Sets the file we are reading
titleSorted = 0 # Counts the collisions for titles
quoteSorted = 0 # Counts the collisions for quotes

# Opens up the file to read
with open(file, 'r', newline = '', encoding = "utf8") as csvfile: 
    # Has the file get read
    reader = csv.reader(csvfile)
    # Starts the clock for title
    titleTime = time.time()
    # Cycles through the rows
    for row1 in reader:

        # Create a DataItem from row
        newTitleItem = DataItem(row1)

        # feed the appropriate field into the hash function to get a key
        # Movie Title hash table
        titleKey = hashFunction(newTitleItem.movieName)
        # Gives us the collisions
        titleSorted += quadProbing(hashTitleTable, titleKey, newTitleItem)

    # Ends the clock for title
    titleEnd = time.time()

    # resets where in the file is being looked at
    # If we didn't do this it would continue to look at the end
    csvfile.seek(0)
    reader = csv.reader(csvfile)

    # Starts the clock for quote
    quoteTime = time.time()
    # Cycles through the rows
    for row2 in reader:
        
        # Create data item for row
        newQuoteItem = DataItem(row2)

        # Movie quote hash table
        quoteKey = hashFunction(newQuoteItem.quote)
        # Gives us the collisions
        quoteSorted += quadProbing(hashQuoteTable, quoteKey, newQuoteItem)
    # Ends the clock for quote
    quoteEnd = time.time()

# Checks how many spaces are wasted for title and quote
titleWasted = sum(1 for x in hashTitleTable if x == None)
quoteWasted = sum(1 for x in hashQuoteTable if x == None)

# Titles
# Prints the collisions, time spent, and spaces wasted
print("Title Collisions: ", titleSorted)
print("Title Time: ", [titleEnd - titleTime])
print("Wasted Title Space: ", titleWasted)

print("") # Just for organization

# Quotes
# Prints the collisions, time spent, and spaces wasted
print("Quote Collisions: ", quoteSorted)    
print("Quote Time: ", [quoteEnd - quoteTime])
print("Wasted Quote Space: ", quoteWasted)



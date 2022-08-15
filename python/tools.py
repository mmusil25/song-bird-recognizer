
import csv
PATH = r'C:\code\ml-playground\song-bird-classifier\bird_info\full-bird-names.csv'

index = []; english = []; latin = []

def indexToBird(anInt):

    with open(PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            index.append(row[0]);
            english.append(row[1])
            latin.append(row[2])

    return english[anInt+1]

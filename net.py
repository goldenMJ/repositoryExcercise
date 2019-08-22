import csv
video = input("video name please")

csvpath = "/Users/seve/Desktop/netflix_ratings.csv"

found = False
#open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #loop through videos
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated" + row[2] + " with a rating of " + row[6] + " .")


            found = True

    if found == False:
        print("sorry, try again")

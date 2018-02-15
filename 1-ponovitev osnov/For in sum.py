
def forandsum():
    total = 0
    for x in range(1,11):
        print x
        total+=x
    print "Vsota je: ",total

forandsum()


listoflists = [["Matt", "Ben", "Jerry"],[1, 2, 3, 4, 5], ["Denmark", "England", "Scotland"]]

for list in listoflists:
    for item in list:
        print item
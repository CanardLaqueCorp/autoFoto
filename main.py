#include random
def main():
    print("Welcome to autoFoto!")
    loadData = input("Would you like to load data from a file? (it should be placed in the data folder) (y/n): ")
    if loadData == "y":
        print("Loading data...")
        #we try to open data/data.json
        try:
            dataFile = open("data/data.json", "r")
            print("Data loaded!")
            print("Starting program...")
            #we close the file
            dataFile.close()
        #if we can't open the file, we print an error message
        except:
            print("Error: couldn't load data.")
            print("Make sure that the data folder exists and that it contains a file named data.json")
    else:
        print("No data loaded, end of program.")
main()


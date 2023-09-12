from src.functions import findImages
import os.path

def main():
    print("Welcome to autoFoto!")
    loadData = input("Would you like to load data from a file? (it should be placed in the data folder) (y/n): ")
    if loadData == "y":
        print("Loading data...")
        #we check if the file exists
        if(os.path.isfile("data/data.json")):
            #we call the function crea() from src/createArrayOfCars.py
            print("Data loaded, scanning for models...")
            findImages()
        else:
            print("The file doesn't exist, end of program.")
            print("make sure the file is in the data folder and it's named data.json")

    else:
        print("No data loaded, end of program.")
main()


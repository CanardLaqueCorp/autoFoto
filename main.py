#include random
def main():
    print("Welcome to autoFoto!")
    loadData = input("Would you like to load data from a file? (it should be placed in the data folder) (y/n): ")
    if loadData == "y":
        print("Loading data...")

    else:
        print("No data loaded, end of program.")
main()
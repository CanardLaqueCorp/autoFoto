import json

def crea():
    dataPath = "data/data.json"
    models = []

    print ("Loading data from " + dataPath + "...")
    with open(dataPath, "r") as f:
        data = json.load(f)

    #we check if the file was loaded correctly
    if data["response"] == "ok":
        print("Data loaded correctly")
    else:
        print("Error loading data")
        return

    for car in data["result"]:
        brand_model = car["brand"] + " " + car["model"]
        print(brand_model)
        models.append(brand_model)
    return 

def findImages():
    print("we generate the array of models")
    modelToFindPhotos = ['']
    modelToFindPhotos=crea()
    print("we search for images of the models")
    print(modelToFindPhotos)

    return

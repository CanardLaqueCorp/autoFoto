import json
#to load images
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import os
import time




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome()
    
#we open google.com
driver.get("https://www.google.com")   
url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")


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
    
    idAlreadyUsed = []
    #we go through every file in the img folder, and we get the id (the name of the file without the extension)
    for filename in os.listdir("img"):
        idAlreadyUsed.append(filename.split(".")[0])
    print("We already have " + str(len(idAlreadyUsed)) + " images", (int(len(idAlreadyUsed))/int(len(data["result"])))*100, "/100 done! of the total")


    



    for car in data["result"]:
        brand_model = car["brand"] + " " + car["model"]
        if str(car["id"]) not in idAlreadyUsed:
            models.append([brand_model, car["id"]])
        
    return models

def load(past, id):
    
    time.sleep(1)
    driver.get(url.format(s='photo{}'.format(past.replace(' ','+'))))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)

    try:
        imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
        src=imgResults[0].get_attribute('src')
        urllib.request.urlretrieve(str(src),"img/{}.jpg".format(id))
    except:
        #we open the file ../errorId.txt and we write the id of the car that we couldn't find
        with open("../errorId.txt", "a") as f:
            f.write(str(id) + "\n")
        print("Error loading image of " + str(id))


    return



def findImages():
    print("we generate the array of models")
    modelToFindPhotos = ['']
    modelToFindPhotos=crea()
    print("we search for images of the models")
    for model in  modelToFindPhotos:
        load(model[0], model[1])
    return



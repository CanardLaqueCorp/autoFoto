import json
#to load images
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time

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
        models.append([brand_model, car["id"]])
    return models

def load(past, id):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome()

    url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")
    driver.get(url.format(s='image{}'.format(past.replace(' ','+'))))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
    imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
    src=imgResults[0].get_attribute('src')
    urllib.request.urlretrieve(str(src),"img/{}.jpg".format(id))
    return

def findImages():
    print("we generate the array of models")
    modelToFindPhotos = ['']
    modelToFindPhotos=crea()
    print("we search for images of the models")
    for model in  modelToFindPhotos:
        load(model[0], model[1])
    return



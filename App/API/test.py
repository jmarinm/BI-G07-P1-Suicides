import json
import requests
import pandas as pd

file = pd.read_csv("App/API/SuicidiosProyecto.csv")


body = {
    "records":[]
}

"""i = 0
for line in file["text"]:
    body["records"].append({"text":line})
    i+= 1
    if i == 1:
        break"""
# api-endpoint
URL = "http://localhost:8000/predict"


body["records"].append({"text":file["text"][1]})
body["records"].append({"text":"aaa"})
# sending get request and saving the response as response object
r = requests.post(url = URL, data = json.dumps(body))
res = r.json()
  
print(res)
import requests
import spacy
from intention import pre_process
nlp = spacy.load('en_core_web_sm')

def extractw(q):
    keywords = pre_process(q)
    print(keywords)
    key = ' '.join(str(k) for k in keywords)
    print(key)
    doc = nlp(key)
    for ent in doc.ents:
        print(ent.label_,ent)
        if (ent.label_ == 'LOC')|(ent.label_ == 'GPE'):
            place = ent.text
            print(place)
            forecast(place)
        else:
            print("Couldnt find the location")
    
def forecast(k):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = k
    url = api_address + city
    json_data = requests.get(url).json()
    desc = json_data['weather'][0]['description']
#    temp = json_data['main']['temp']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    min_temp = json_data['main']['temp_min']
    max_temp = json_data['main']['temp']
    print(" the temperature ranges from ",min_temp ," and ", max_temp ," with humidity of ", humidity ," and pressure ", pressure)
    print("forecast:",desc)
    

#extractw("weather in ECIL?")
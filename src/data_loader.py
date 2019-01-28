import json
import urllib.request
import time


class DataLoader:

    def __init__(self):
        self.city_ids = {}
        self.city_ids = {
            "Warszawa": 6695624,
            "Kraków": 3094802,
            "Łódź": 3093133,
            "Wrocław": 3081368,
            "Poznań": 7530858,
            "Gdańsk": 7531002,
            "Rzeszów": 759734,
            "Szczecin": 3083829,
            "Opole": 3090048,
            "Płock": 3088825,
            "Olsztyn": 763166,
            "Gdynia": 3099424,
            "Legnica": 7530968,
            "Gliwice": 3099230,
            "Bielsko-Biała": 7532925,
            "Toruń": 3083271,
            "Elblag": 3099759,
            "Lublin": 765876,
            "Zabrze": 7530952,
            "Zakopane": 7531513,
            "Sopot": 7531444,
            "Suwałki": 7531587,
            "Bydgoszcz": 3102014,
            "Białystok": 776069,
            "Katowice": 3096472,
            "Częstochowa": 7530964,
            "Radom": 7530982,
            "Sosnowiec": 7530975,
            "Kielce": 769250
        }
        self.city_info = {}
        self.cell_map = []


    #returns json dictionary from given city_id
    #city_id can be found by executing command DataLoader().city_ids["city_name"]
    def load_city_data(self, city_name="none", city_id=0):
        if city_id != 0:
            data = urllib.request.urlopen(
                "https://api.openweathermap.org/data/2.5/forecast?id=" + str(city_id)
                + "&APPID=601d44c731385ddeec00b5011fcbe441&units=metric").read()
        elif city_name != "none":
            city_id = self.city_ids[city_name]
            data = urllib.request.urlopen(
                "https://api.openweathermap.org/data/2.5/forecast?id=" + str(city_id)
                + "&APPID=601d44c731385ddeec00b5011fcbe441&units=metric").read()
        else:
            return "Wrong Parameters"
        return json.loads(data)

    def load_whole_city_data(self):
        city_data = {}
        start_time = time.time()
        length = len(self.city_ids.keys())
        iterator = 1.0
        print("Started downloading forecast data...")
        for city_name in self.city_ids.keys():
            city_data[city_name] = self.load_city_data(city_name=city_name)
            print("Download progress: {0:.0f}%...".format((iterator/length)*100))
            iterator += 1
        end_time = time.time()
        print("Finished forecast data download in {}s.".format(end_time - start_time))
        return city_data

    def initialize(self):
        self.city_info = self.load_whole_city_data()
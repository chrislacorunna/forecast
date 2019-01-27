from src import DataLoader


class DataProcessor:


    def __init__(self):
        self.data = DataLoader()
        self.data.initialize()

    #returns list of dates in range (current_date_time, 5_days_later_date_time) with a step of 3 hours
    def get_list_of_dates(self):
        date_list = []
        for i in range(0, 39):
            date_list.append(self.data.city_info["Warszawa"]["list"][i]['dt_txt'])
        return date_list

    #returns dictionary: {'2019-01-26 21:00:00': -6.07, '2019-01-27 00:00:00': -5.53,...
    def get_temperature_dict(self, city_name):
        temperature_list = {}
        for i in range(0,39):
            temperature_list[self.data.city_info[city_name]["list"][i]['dt_txt']] =\
                self.data.city_info[city_name]["list"][i]['main']['temp']
        return temperature_list

    #returns dicitionary: {'2019-01-26 21:00:00': 88, '2019-01-27 00:00:00': 92, '2019-01-27 03:00:00': 92,...
    def get_humidity_dict(self, city_name):
        humidity_list = {}
        for i in range(0,39):
            humidity_list[self.data.city_info[city_name]["list"][i]['dt_txt']] =\
                self.data.city_info[city_name]["list"][i]['main']['humidity']
        return humidity_list


    #returns dictionary: {'2019-01-26 21:00:00': {'speed': 2.22, 'deg': 126.001}, '2019-01-27 00:00:00': {'speed': 2.07, 'deg': 119.001},..
    def get_wind_dict(self, city_name):
        wind_list = {}
        for i in range(0, 39):
            wind_list[self.data.city_info[city_name]["list"][i]['dt_txt']] = \
                self.data.city_info[city_name]["list"][i]['wind']
        return wind_list

    #returns dicitionary with pairs {'date_time', 'cloudiness_%'}
    def get_cloudiness_dict(self, city_name):
        cloud_list = {}
        for i in range(0, 39):
            cloud_list[self.data.city_info[city_name]["list"][i]['dt_txt']] = \
                self.data.city_info[city_name]["list"][i]['clouds']['all']
        return cloud_list
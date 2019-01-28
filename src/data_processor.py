from src import DataLoader
from statistics import mean

class DataProcessor:


    def __init__(self):
        self.data = DataLoader()
        self.data.initialize()

    #returns current date
    def get_current_date(self):
        return self.get_list_of_dates()[0]

    # returns list of dates in range (current_date_time, 5_days_later_date_time) with a step of 3 hours
    def get_list_of_dates_and_time(self):
        date_list = []
        for i in range(0, 39):
            date_list.append(self.data.city_info["Warszawa"]["list"][i]['dt_txt'])
        return date_list

    def get_list_of_dates(self):
        date_list = []
        p_list = self.get_list_of_dates_and_time()
        previous = ""
        for datetime in p_list:
            d, t = datetime.split()
            if previous == "" or not previous == d:
                date_list.append(d)
        return list(set(date_list))


    #returns dictionary: {'2019-01-26 21:00:00': -6.07, '2019-01-27 00:00:00': -5.53,...
    def get_temperature_dict(self, city_name):
        temperature_list = {}
        for i in range(0,39):
            temperature_list[self.data.city_info[city_name]["list"][i]['dt_txt']] =\
                self.data.city_info[city_name]["list"][i]['main']['temp']
        return temperature_list

    def get_temperature_list_for_date(self, date, city_name):
        tmp_list = []
        for k, v in self.get_temperature_dict(city_name).items():
            if date in k:
                tmp_list.append(v)
        return tmp_list

    # returns dictionary: {'2019-01-26 21:00:00': -6.07, '2019-01-27 00:00:00': -5.53,...
    def get_pressure_dict(self, city_name):
        temperature_list = {}
        for i in range(0, 39):
            temperature_list[self.data.city_info[city_name]["list"][i]['dt_txt']] = \
                self.data.city_info[city_name]["list"][i]['main']['pressure']
        return temperature_list

    def get_pressure_for_date(self, date, city_name):
        tmp_list = []
        for k, v in self.get_pressure_dict(city_name).items():
            if date in k:
                tmp_list.append(v)
        return "{0:.2f}".format(mean(tmp_list))

    # returns dictionary: {'2019-01-26 21:00:00': -6.07, '2019-01-27 00:00:00': -5.53,...
    def get_sea_level_dict(self, city_name):
        temperature_list = {}
        for i in range(0, 39):
            temperature_list[self.data.city_info[city_name]["list"][i]['dt_txt']] = \
                self.data.city_info[city_name]["list"][i]['main']['sea_level']
        return temperature_list

    def get_sea_level_for_date(self, date, city_name):
        tmp_list = []
        for k, v in self.get_sea_level_dict(city_name).items():
            if date in k:
                tmp_list.append(v)
        return "{0:.2f}".format(mean(tmp_list))

    #returns dicitionary: {'2019-01-26 21:00:00': 88, '2019-01-27 00:00:00': 92, '2019-01-27 03:00:00': 92,...
    def get_humidity_dict(self, city_name):
        humidity_list = {}
        for i in range(0,39):
            humidity_list[self.data.city_info[city_name]["list"][i]['dt_txt']] =\
                self.data.city_info[city_name]["list"][i]['main']['humidity']
        return humidity_list

    def get_humidity_list_for_date(self, date, city_name):
        tmp_list = []
        for k, v in self.get_humidity_dict(city_name).items():
            if date in k:
                tmp_list.append(v)
        return tmp_list


    #returns dictionary: {'2019-01-26 21:00:00': {'speed': 2.22, 'deg': 126.001}, '2019-01-27 00:00:00': {'speed': 2.07, 'deg': 119.001},..
    def get_wind_dict(self, city_name):
        wind_list = {}
        for i in range(0, 39):
            wind_list[self.data.city_info[city_name]["list"][i]['dt_txt']] = \
                self.data.city_info[city_name]["list"][i]['wind']
        return wind_list

    def get_wind_list(self, city_name):
        tmp_list = []
        for k, v in self.get_wind_dict(city_name).items():
                tmp_list.append(v['speed'])
        return tmp_list

    def get_wind_list_for_date(self, date, city_name):
        tmp_list = []
        for k, v in self.get_wind_dict(city_name).items():
            if date in k:
                tmp_list.append(v)
        return tmp_list

    def get_wind_strength_for_date(self, date, city_name):
        tmp_list = []
        for k, v in self.get_wind_dict(city_name).items():
            if date in k:
                tmp_list.append(v['speed'])
        return tmp_list

    #returns dicitionary with pairs {'date_time', 'cloudiness_%'}
    def get_cloudiness_dict(self, city_name):
        cloud_list = {}
        for i in range(0, 39):
            cloud_list[self.data.city_info[city_name]["list"][i]['dt_txt']] = \
                self.data.city_info[city_name]["list"][i]['clouds']['all']
        return cloud_list

    def get_cloudiness_list_for_date(self, date, city_name):
        tmp_list = []
        for k, v in self.get_cloudiness_dict(city_name).items():
            if date in k:
                tmp_list.append(v)
        return tmp_list

    #returns weather description
    def get_weather_description_dict(self, city_name):
        desc_list = {}
        for i in range(0, 39):
            desc_list[self.data.city_info[city_name]["list"][i]['dt_txt']] = \
                self.data.city_info[city_name]["list"][i]['weather'][0]['description']
        return desc_list

    def get_weather_list_for_date(self, date, city_name):
        tmp_list = dict()
        for k, v in self.get_weather_description_dict(city_name).items():
            if date in k:
                tmp_list[k] = v
        return tmp_list

    def convert_to_float(self, list_to_convert):
        tmp_list = []
        for v in list(list_to_convert):
            tmp_list.append(float(v))
        return tmp_list

    def get_weather_stat_string_for_date(self, city_name, date):
        max_temp = max(self.convert_to_float(self.get_temperature_list_for_date(date, city_name)))
        min_temp = min(self.convert_to_float(self.get_temperature_list_for_date(date, city_name)))
        avg_temp = mean(self.convert_to_float(self.get_temperature_list_for_date(date, city_name)))
        wind = mean(self.convert_to_float(self.get_wind_strength_for_date(date, city_name)))
        gusts = mean(self.convert_to_float(self.get_wind_strength_for_date(date, city_name)))
        clouds = mean(self.convert_to_float(self.get_cloudiness_list_for_date(date, city_name)))

        a = ""
        a += "Date: " + date + "\n"
        a += "Maximum temperature:   " + "{0:.1f}".format(max_temp) + "°C\n"
        a += "Minimum temperature:    " + "{0:.1f}".format(min_temp) + "°C\n"
        a += "Average temperature:    " + "{0:.1f}".format(avg_temp) + "°C\n"
        a += "Wind:                               " + "{0:.2f}".format(wind) + "m/s\n"
        a += "Gusts of wind:                 " + "{0:.2f}".format(gusts) + "m/s\n"
        a += "Cloudiness:                      " + "{0:.1f}".format(clouds) + "%\n"

        return a

    def get_xticks(self):
        tab = []

        for val in self.get_list_of_dates():
            k = val.split('-')
            k = k[2] + "." + k[1]
            tab.append(k)
            tab.append("")
            tab.append("")
            tab.append("")
            tab.append("")
            tab.append("")
            tab.append("")
            tab.append("")
        return tab

    def get_additional_info_string(self, city_name, date):
        a = ""
        a += "Pressure:         " + str(self.get_pressure_for_date(date, city_name)) + "hPa\n"
        a += "Sea level:        " + str(self.get_sea_level_for_date(date, city_name)) + "hPa\n"
        a += "City info:\n"
        a += "     City:            " + str(self.data.city_info[city_name]['city']['name']) + "\n"
        a += "     Country:      " + str(self.data.city_info[city_name]['city']['country']) + "\n"
        a += "     Latitude:      " + str(self.data.city_info[city_name]['city']['coord']['lat']) + "\n"
        a += "     Longtitude:  " + str(self.data.city_info[city_name]['city']['coord']['lon']) + "\n"
        return a

    def get_weather_desc_string_for_date(self, city_name, date):
        weather = ""
        for k, v in self.get_weather_list_for_date(date, city_name).items():
            weather += k.split()[1] + ": " + v + "\n"
        return weather
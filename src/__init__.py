from src.data_loader import DataLoader
from src.data_processor import DataProcessor

data = DataProcessor()
print(data.get_temperature_dict("Warszawa"))
print(data.get_humidity_dict("Warszawa"))
print(data.get_wind_dict("Warszawa"))
print(data.get_cloudiness_dict("Warszawa"))



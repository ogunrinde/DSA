class WeatherAnalysis():
    def __init__(self):
        self.weather = {}
        self.temperature = []

    def load_weather_data(self):
        with open("nyc_weather.csv","r") as f:
            for line in f:
                data = line.split(',')
                day = data[0]
                temp = data[1]
                if day != 'date':
                    self.weather[day] = float(temp)
                    self.temperature.append(float(temp))


    def avg_temperature_in_first_week(self):
       return sum(self.temperature[0:7]) / len(self.temperature[0:7])

    def maximum_temperature_in_first_10_days(self):
        return max(self.temperature[0:10])

if __name__ == "__main__":
    w = WeatherAnalysis()
    w.load_weather_data()
    print(w.avg_temperature_in_first_week())
    print(w.maximum_temperature_in_first_10_days())
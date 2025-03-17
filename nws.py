import time

import requests
import json
import nwsClasses


class NWS:
    lat = 41.7646
    lon = -88.3110
    radarStation = 'KLOT'
    forecast: nwsClasses.forecastObj = None
    forecastHourly: nwsClasses.forecastObj = None
    forecast_url = "https://api.weather.gov/gridpoints/LOT/53,67/forecast",
    forecastHourly_url = "https://api.weather.gov/gridpoints/LOT/53,67/forecast/hourly",
    alerts_all: nwsClasses.alertsObj = None
    alerts_active: nwsClasses.alertsObj = None
    latestObserve: nwsClasses.latestObserve = None
    city = 'Aurora'
    state = 'IL'

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.setup()

    def setup(self):
        # print('Updating NWS Endpoints')
        weather = f'https://api.weather.gov/points/{self.lat},{self.lon}'
        resp = requests.get(weather)
        data = json.loads(resp.text)
        self.radarStation = data['properties']['radarStation']
        self.forecast_url = data['properties']['forecast']
        self.forecastHourly_url = data['properties']['forecastHourly']
        self.city = data['properties']['relativeLocation']['properties']['city']
        self.state = data['properties']['relativeLocation']['properties']['state']

        self.forecast = nwsClasses.forecastObj(self.forecast_url)
        self.forecastHourly = nwsClasses.forecastObj(self.forecastHourly_url)
        self.alerts_all = nwsClasses.alertsObj(self.lat, self.lon, False)
        self.alerts_active = nwsClasses.alertsObj(self.lat, self.lon, True)
        self.latestObserve = nwsClasses.latestObserve(self.radarStation)


if __name__ == '__main__':
    import convertUSA

    latitude = 41.7646
    longitude = -88.3110
    a = NWS(latitude, longitude)
    print(f'{a.city} {a.state}')
    print(f'Total Alerts: {len(a.alerts_all.features)}')
    print(f'Active Alerts: {len(a.alerts_active.features)}')
    f = convertUSA.c_to_f(a.latestObserve.temperature)
    print(f'Current Temp: {f}F')

    for b in range(0, 3):
        c = a.alerts_all.features[b]
        print(c.headline)
        # print(c.description)
        time.sleep(1)

    print(f'\n *** {a.alerts_all.features[0].headline} ***')
    print('* Area')
    print(f'{a.alerts_all.features[0].areaDesc}')
    print(f'* Ending: {a.alerts_all.features[0].expires}')
    print('* Description')
    print(f'{a.alerts_all.features[0].description}')

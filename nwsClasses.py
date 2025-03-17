import requests
import json


class featureObj:
    id = ''
    areaDesc = "District of Columbia; Washington"
    sent = "2025-03-16T18:02:00-04:00"
    effective = "2025-03-16T18:02:00-04:00"
    onset = "2025-03-16T18:02:00-04:00"
    expires = "2025-03-16T19:15:00-04:00"
    ends = "2025-03-16T18:00:00-04:00"
    status = "Actual"
    messageType = "Alert"
    category = "Met"
    severity = "Moderate"
    certainty = "Likely"
    urgency = "Expected"
    event = "Wind Advisory"
    sender = "w-nws.webmaster@noaa.gov"
    senderName = "NWS Baltimore MD/Washington DC"
    headline = "Wind Advisory issued March 16 at 6:02PM EDT until March 16 at 6:00PM EDT by NWS Baltimore MD/Washington DC"
    description = "Southerly winds will remain gusty this evening, but gusts should top\nout around 30 to 40 mph."
    instruction = None
    response = "Execute"
    parameters = {
        "AWIPSidentifier": ["NPWLWX"],
        "WMOidentifier": ["WWUS71 KLWX 162202"],
        "NWSheadline": ["WIND ADVISORY HAS EXPIRED"],
        "BLOCKCHANNEL": ["EAS", "NWEM", "CMAS"],
        "VTEC": ["/O.EXP.KLWX.WI.Y.0011.000000T0000Z-250316T2200Z/"],
        "eventEndingTime": ["2025-03-16T22:00:00+00:00"],
        "expiredReferences": [
            "w-nws.webmaster@noaa.gov,urn:oid:2.49.0.1.840.0.2b65efc75d8b13ccaab6b47159e3cf81d8fd788f.001.1,2025-03-16T09:48:00-04:00 w-nws.webmaster@noaa.gov,urn:oid:2.49.0.1.840.0.6f00d2df55230702a4523a8f2a64cf2a472a8422.003.1,2025-03-16T15:34:00-04:00 w-nws.webmaster@noaa.gov,urn:oid:2.49.0.1.840.0.6f00d2df55230702a4523a8f2a64cf2a472a8422.002.1,2025-03-16T15:34:00-04:00 w-nws.webmaster@noaa.gov,urn:oid:2.49.0.1.840.0.98f49bebb228356e5ea931e22be510216dbcba53.003.1,2025-03-16T12:59:00-04:00 w-nws.webmaster@noaa.gov,urn:oid:2.49.0.1.840.0.98f49bebb228356e5ea931e22be510216dbcba53.001.1,2025-03-16T12:59:00-04:00"]
    }

    def __init__(self, data):
        self.id = data['id']
        self.areaDesc = data['areaDesc']
        self.sent = data['sent']
        self.effective = data['effective']
        self.onset = data['onset']
        self.expires = data['expires']
        self.ends = data['ends']
        self.status = data['status']
        self.messageType = data['messageType']
        self.category = data['category']
        self.severity = data['severity']
        self.certainty = data['certainty']
        self.urgency = data['urgency']
        self.event = data['event']
        self.sender = data['sender']
        self.senderName = data['senderName']
        self.headline = data['headline']
        self.description = data['description']
        self.instruction = data['instruction']
        self.response = data['response']
        self.parameters = data['parameters']


class periodObj:
    number = 1
    name = "Tonight"
    startTime = "2025-03-16T19:00:00-05:00"
    endTime = "2025-03-17T06:00:00-05:00"
    isDaytime = False
    temperature = 23
    temperatureUnit = "F"
    temperatureTrend = ""
    probabilityOfPrecipitation = {"unitCode": "wmoUnit:percent", "value": None}
    windSpeed = "0 to 5 mph"
    windDirection = "W"
    icon = "https://api.weather.gov/icons/land/night/few?size=medium"
    shortForecast = "Mostly Clear"
    detailedForecast = "Mostly clear, with a low around 23. West wind 0 to 5 mph."

    # The following are only in hourly forecast periods
    dewpoint = {"unitCode": "wmoUnit:degC", "value": -6.111111111111111}
    relativeHumidity = {"unitCode": "wmoUnit:percent", "value": 63}

    def __init__(self, data):
        self.number = data['number']
        self.name = data['name']
        self.startTime = data['startTime']
        self.endTime = data['endTime']
        self.isDaytime = data['isDaytime']
        self.temperature = data['temperature']
        self.temperatureUnit = data['temperatureUnit']
        self.temperatureTrend = data['temperatureTrend']
        self.probabilityOfPrecipitation = data['probabilityOfPrecipitation']
        self.windSpeed = data['windSpeed']
        self.windDirection = data['windDirection']
        self.icon = data['icon']
        self.shortForecast = data['shortForecast']
        self.detailedForecast = data['detailedForecast']

        # The following are only in hourly forecast periods
        if 'dewpoint' in data.keys():
            self.dewpoint = data['dewpoint']
        else:
            self.dewpoint = {}
        if 'relativeHumidity' in data.keys():
            self.relativeHumidity = data['relativeHumidity']
        else:
            self.relativeHumidity = {}


class forecastObj:
    url = 'https://api.weather.gov/gridpoints/LOT/53,67/forecast'
    generatedAt = "2025-03-17T00:31:51+00:00"
    updateTime = "2025-03-17T00:06:45+00:00"
    validTimes = "2025-03-16T18:00:00+00:00/P7DT7H"
    periods = []

    def __init__(self, url):
        self.url = url
        self.update()

    def update(self):
        if 'hourly' in self.url:
            # print("Updating Hourly Forecast")
            pass
        else:
            # print("Updating Daily Forecast")
            pass
        resp = requests.get(self.url)
        data = json.loads(resp.text)
        self.generatedAt = data['properties']['generatedAt']
        self.updateTime = data['properties']['updateTime']
        self.validTimes = data['properties']['validTimes']
        self.periods = []
        for p in data['properties']['periods']:
            self.periods.append(periodObj(p))


class alertsObj:
    only_acive = True
    lat = 41.7646
    lon = -88.3110
    features = []
    title = "Current watches, warnings, and advisories for 38.9807 N, 76.9373 W"
    updated = "2025-03-16T22:03:11+00:00"

    def __init__(self, lat, lon, only_active=True):
        self.only_acive = only_active
        self.lat = lat
        self.lon = lon
        self.update()

    def update(self):
        if self.only_acive:
            r = f'https://api.weather.gov/alerts/active?point={self.lat},{self.lon}'
            # print('Updating Active Alerts')
        else:
            r = f'https://api.weather.gov/alerts?point={self.lat},{self.lon}'
            # print('Updating All Alerts')
        resp = requests.get(r)
        data = json.loads(resp.text)
        self.title = data['title']
        self.updated = data['updated']
        self.features = []
        for f in data['features']:
            self.features.append(featureObj(f['properties']))


class latestObserve:
    station = "KLOT"

    timestamp = "2025-03-17T02:10:00+00:00"
    textDescription = "Mostly Clear"
    icon = "https://api.weather.gov/icons/land/night/few?size=medium"
    presentWeather = []
    temperature = -2
    dewpoint = -3
    windDirection = 180
    windSpeed = 9.36
    windGust = None
    barometricPressure = 101660
    seaLevelPressure = None
    visibility = 16090
    maxTemperatureLast24Hours = None
    minTemperatureLast24Hours = None
    precipitationLastHour = None
    precipitationLast3Hours = None
    precipitationLast6Hours = None
    relativeHumidity = 92.863965557739
    windChill = -5.500160729851666
    heatIndex = None
    cloudLayers = [{"base": {"unitCode": "wmoUnit:m", "value": 1980}, "amount": "FEW"}]

    def __init__(self, station):
        self.station = station
        self.update()

    def update(self):
        # print('Updating Current Weather')
        url = f'https://api.weather.gov/stations/{self.station}/observations/latest'
        resp = requests.get(url)
        data = json.loads(resp.text)

        self.timestamp = data['properties']['timestamp']
        self.textDescription = data['properties']['textDescription']
        self.icon = data['properties']['icon']
        self.presentWeather = data['properties']['presentWeather']
        self.temperature = data['properties']['temperature']['value']
        self.dewpoint = data['properties']['dewpoint']['value']
        self.windDirection = data['properties']['windDirection']['value']
        self.windSpeed = data['properties']['windSpeed']['value']
        self.windGust = data['properties']['windGust']['value']
        self.barometricPressure = data['properties']['barometricPressure']['value']
        self.seaLevelPressure = data['properties']['seaLevelPressure']['value']
        self.visibility = data['properties']['visibility']['value']
        self.maxTemperatureLast24Hours = data['properties']['maxTemperatureLast24Hours']['value']
        self.minTemperatureLast24Hours = data['properties']['minTemperatureLast24Hours']['value']
        self.precipitationLastHour = data['properties']['precipitationLastHour']['value']
        self.precipitationLast3Hours = data['properties']['precipitationLast3Hours']['value']
        self.precipitationLast6Hours = data['properties']['precipitationLast6Hours']['value']
        self.relativeHumidity = data['properties']['relativeHumidity']['value']
        self.windChill = data['properties']['windChill']['value']
        self.heatIndex = data['properties']['heatIndex']['value']
        self.cloudLayers = data['properties']['cloudLayers']

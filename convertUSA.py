def c_to_f(temp):
    return (temp * 1.8) + 32


def mm_to_inch(mm):
    return mm / 25.4


def km_to_miles(km):
    return km / 1.6093445


def degrees_to_cardinal(d):
    '''
    note: this is highly approximate...
    '''
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((d + 11.25) / 22.5)
    return dirs[ix % 16]

from nws import NWS
from convertUSA import c_to_f
import term_colors

color1 = term_colors.Black + term_colors.On_Green
color2 = term_colors.Red
color3 = term_colors.Black + term_colors.On_White
color_reset = term_colors.Color_Off


def printc(color, text, end=None):
    print(f'{color}{text}{term_colors.Color_Off}', end=end)


def main_help():
    printc(color3, '*** Commands ***')
    print('c, current - Current Weather')
    print('a, alerts - Alerts Menu')
    print('q, quit - Exit the program')
    print('?, h, help - Display This Help Menu')


def current(w: NWS):
    w.latestObserve.update()
    printc(color1, '*** Current Weather ***')
    print(f'{w.latestObserve.timestamp}')
    print(f'Temp: {w.latestObserve.temperature}C / {c_to_f(w.latestObserve.temperature)}F')
    print(f'Dewpoint: {w.latestObserve.dewpoint}C / {c_to_f(w.latestObserve.dewpoint)}F')
    print(f'{w.latestObserve.textDescription}')


def alerts(w: NWS):
    w.alerts_all.update()
    w.alerts_active.update()
    printc(color3, '*** Alerts ***')
    print(f'Active: {len(w.alerts_active.features)}')
    print(f'Total: {len(w.alerts_all.features)}')
    loop = True
    while loop:
        _i = input('\nAlerts: >')
        print('')
        if _i.lower() in ['q', 'quit']:
            loop = False
        elif _i.lower() in ['a', 'active']:
            print(f'Active Alerts: {len(w.alerts_active.features)}\n')
            if len(w.alerts_active.features) > 0:
                for a in range(0, len(w.alerts_active.features)):
                    print(f'({a}) {w.alerts_active.features[a].headline}')
                _i = input('\nSelect: >')
                try:
                    print(w.alerts_active.features[int(_i)].description)
                except ValueError:
                    pass
        elif _i.lower() in ['r', 'recent']:
            print(f'Recent Alerts: {len(w.alerts_all.features)}\n')
            if len(w.alerts_all.features) < 20:
                end = len(w.alerts_all.features)
            else:
                end = 20
            for a in range(0, end):
                print(f'({a}) {w.alerts_all.features[a].headline}')
            _i = input('\nSelect: >')
            try:
                f = w.alerts_all.features[int(_i)]
                print(f'\n*** {f.headline} ***')
                print(f'Expires: {f.expires}')
                print('Description')
                print(f'{f.description}\n')
            except ValueError:
                pass
        elif _i.lower() in ['?', 'h', 'help']:
            printc(color3, 'Alerts Help')
            print('a, active - List Active Alerts')
            print('r, recent - List Recent Alerts')
            print('q, quit - Exit Alerts')
            print('?, h, help - This Help Menu')
        elif _i == '':
            pass
        else:
            print(f'( {color2}{_i}{color_reset} ) Unknown Command! Try "?" for help.')


if __name__ == '__main__':
    latitude = 41.7646
    longitude = -88.3110
    print('\nNWS Tools by KD9YQK')
    print('Loading...', end='')
    weather = NWS(latitude, longitude)
    print('OK\n')
    current(weather)
    while True:
        i = input('\nCommand: >')
        print('')
        if i.lower() in ['?', 'h', 'help']:
            main_help()
        elif i.lower() in ['c', 'current']:
            current(weather)
        elif i.lower() in ['a', 'alerts']:
            alerts(weather)
        elif i.lower() in ['q', 'quit']:
            exit()
        elif i == '':
            pass
        else:
            print(f'( {color2}{i}{color_reset} ) Unknown Command! Try "?" for help.')

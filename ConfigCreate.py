from configparser import ConfigParser
config = ConfigParser()
cfgfile = "config.ini"

def cfgWrite():
    config.add_section('main')
    config.set('main', 'x_init', '100')
    config.set('main', 'y_init', '100')
    config.set('main', 'width', '600')
    config.set('main', 'height', '400')
    with open('config.ini', 'w') as f:
        config.write(f)
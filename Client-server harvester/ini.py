import configparser

def ini():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'AdresWWW': 'https://zsem.edu.pl' #https://www.nowy-sacz.so.gov.pl
                        }

    with open('cfg.ini', 'w') as configfile:
        config.write(configfile)


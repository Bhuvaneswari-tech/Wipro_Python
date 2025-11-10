import configparser

config = configparser.ConfigParser()
config['Database'] = {'host': 'localhost', 'port': '3306'}
with open('config.ini', 'w') as f:
    config.write(f)
print("Config file created.")

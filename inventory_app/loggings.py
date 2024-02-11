import logging
import configparser



config = configparser.ConfigParser()
config.read('./inventory_app/config.ini')
_path_log = './inventory_app/logs/app.log' #config['DEFAULT']['path_logs']
#_path_log = config['DEFAULT']['path_logs']

logging.basicConfig(filename=_path_log, filemode='a'
                    , level=logging.DEBUG
                    , format='%(asctime)s -%(levelname)s- %(message)s'
                    , datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Request API')
log = logging 
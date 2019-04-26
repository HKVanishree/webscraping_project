from logging.handlers import RotatingFileHandler
import configparser
import logging


class loggerModule:
  def logging(self):
    """Get log level from config file"""
    config = configparser.ConfigParser()
    config.read('ConfigFile.ini')
    LogLevel = config.get('LOGLEVEL', 'log')

    """"Add formatters to looger object"""
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
    logger = logging.getLogger('example_logger')
    Rthandler = RotatingFileHandler('log/webScrap.log', maxBytes=500, backupCount=5)

    if LogLevel == 'debug':
        logger.setLevel(logging.DEBUG)
    if LogLevel == 'info':
        logger.setLevel(logging.INFO)
    if LogLevel == 'error':
        logger.setLevel(logging.ERROR)
    if LogLevel == 'critical':
        logger.setLevel(logging.CRITICAL)


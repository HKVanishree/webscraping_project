from bs4 import BeautifulSoup
import requests
import logging
from logging.handlers import RotatingFileHandler
import configparser
import re
import validators

config = configparser.ConfigParser()
config.read('ConfigFile.ini')

keyWordsList = config.get('KEYWORD', 'k1')
keyWords = keyWordsList.split(",")

LogLevel = config.get('LOGLEVEL', 'log')

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
logger = logging.getLogger('example_logger')
Rthandler = RotatingFileHandler('log/webScrap.log', maxBytes=500, backupCount=5)

#Rthandler.setLevel(logging.INFO)

if LogLevel == 'debug':
    logger.setLevel(logging.DEBUG)
if LogLevel == 'info':
    logger.setLevel(logging.INFO)
if LogLevel == 'error':
    logger.setLevel(logging.ERROR)
if LogLevel == 'critical':
    logger.setLevel(logging.CRITICAL)

print("Effective logging level is {}".format(
    logging.getLevelName(logger.getEffectiveLevel())))
logger.info("Effective logging level is {}".format(
    logging.getLevelName(logger.getEffectiveLevel())))

formatter = logging.Formatter('%(asctime)-12s [%(levelname)s] %(message)s')
Rthandler.setFormatter(formatter)
logger.addHandler(Rthandler)

urlList = config.get('URL', 'url')
urlsList = urlList.split(",")

f = open("Output.csv", "w")

for url in urlsList:

    logger.info(str("Scraping url "+url))
    f.write("\nURL:" + url + ",\n")
    print("URL: ", url)
    for k in keyWords:
        if not validators.url(url):
            print("Invalid url: ", url)
            logger.error(str("Invalid URL"+url))
        try:
            r = requests.get(url)
        except Exception as e:
            print("Name or service not known for", url)
            logger.critical(str(e))
            exit(1)

        soup = BeautifulSoup(r.content, "html.parser")
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText()
        y = len(re.findall(str(" "+k+" "), visible_text))
        output = "Keyword: " + str(k) + ", count: " + str(y)+"\n"
        logger.warning("Count written to output file")
        f.write(output)
        print("Keyword:", k, " count:", y)

f.close()

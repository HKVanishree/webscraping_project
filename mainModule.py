import configparser
from webScrapping import scrapping
import logging

def main():
    """Get list of keywords and urls from the configuration file"""
    try:
     config = configparser.ConfigParser()
     config.read('ConfigFile.ini')
    except Exception as e:
        print("Manual errors found in the configuration file\n")
        exit(1)
    keyWordsList = config.get('KEYWORD', 'k1')
    keyWords = keyWordsList.split(",")

    urlList = config.get('URL', 'url')
    urlsList = urlList.split(",")

    """Get logger object"""

    logger = logging.getLogger('example_logger')

    """Send the list of keywords, urls and logger to  get the count of keywords"""

    scrapping(keyWords, urlsList, logger)


if __name__ == '__main__':
    main()


import configparser
from webScrapping import scrapping

def main():
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

    scrapping(keyWords, urlsList)


if __name__ == '__main__':
    main()


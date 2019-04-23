import configparser
from webScrapping import scrapping

def main():
    config = configparser.ConfigParser()
    config.read('ConfigFile.ini')
    print("Inside main")
    keyWordsList = config.get('KEYWORD', 'k1')
    keyWords = keyWordsList.split(",")

    urlList = config.get('URL', 'url')
    urlsList = urlList.split(",")

    scrapping(keyWords, urlsList)


if __name__ == '__main__':
    main()


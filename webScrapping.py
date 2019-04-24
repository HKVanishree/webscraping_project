from bs4 import BeautifulSoup
import requests
import re
import validators



def scrapping(keyWords,urlsList,logger):


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








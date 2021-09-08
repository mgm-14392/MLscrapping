import bs4
import requests

## Check agent!!
def make_soup(url):
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:91.0) Gecko/20100101 Firefox/91.0"
    page = requests.get(url, headers={'User-Agent': agent})
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    return soup
